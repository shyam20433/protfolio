from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId
import os
from datetime import datetime

app = Flask(__name__)


try:
    client = MongoClient(os.getenv("MONGODB_URI"))
    # Test the connection
    client.admin.command('ping')
    db = client.portfolio
    projects_collection = db.projects
    portfolio_collection = db.portfolio
    print("✅ MongoDB connected successfully!")
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")
    print("⚠️  App will run without database functionality")
    projects_collection = None
    portfolio_collection = None

def normalize_projects(raw_projects):
    """Normalize project objects to the keys used by the template."""
    normalized = []
    for item in (raw_projects or []):
        if not isinstance(item, dict):
            continue
        title = item.get('title') or item.get('name') or item.get('project_title') or ''
        category = item.get('category') or item.get('type') or item.get('tag') or 'Other'
        description = item.get('description') or item.get('desc') or item.get('about') or ''
        technologies = item.get('technologies') or item.get('tech') or item.get('tech_stack') or []
        if isinstance(technologies, str):
            technologies = [t.strip() for t in technologies.split(',') if t.strip()]
        # Image mapping and path cleanup
        image = item.get('image') or item.get('img') or item.get('thumbnail') or item.get('image_url') or ''
        if isinstance(image, str) and image:
            img = image.replace('\\', '/')
            if 'static/' in img:
                img = img.split('static/', 1)[1]
            image = img.lstrip('/')
        # Links
        github_url = item.get('github_url') or item.get('github') or item.get('repo') or ''
        live_url = item.get('live_url') or item.get('live') or item.get('demo') or item.get('demo_url') or ''
        # Ensure _id string
        project_id = item.get('_id')
        if isinstance(project_id, ObjectId):
            project_id = str(project_id)
        normalized.append({
            '_id': project_id,
            'title': title,
            'category': category,
            'description': description,
            'technologies': technologies if isinstance(technologies, list) else [],
            'image': image,
            'github_url': github_url,
            'live_url': live_url,
        })
    return normalized

def get_projects_from_db():
    """Get projects: use embedded projects only if non-empty; otherwise fallback to collection."""
    try:
        portfolio_doc = get_portfolio_from_db()
        if portfolio_doc:
            embedded = portfolio_doc.get('projects')
            if isinstance(embedded, list) and len(embedded) > 0:
                for project in embedded:
                    if isinstance(project, dict) and isinstance(project.get('_id'), ObjectId):
                        project['_id'] = str(project['_id'])
                return normalize_projects(embedded)
    except Exception as e:
        print(f"Error reading embedded projects: {e}")

    if projects_collection is not None:
        try:
            projects = list(projects_collection.find())
            for project in projects:
                project['_id'] = str(project['_id'])
            return normalize_projects(projects)
        except Exception as e:
            print(f"Error fetching projects from collection: {e}")
            return []
    return []

def get_portfolio_from_db():
    """Get the latest portfolio document from MongoDB."""
    if 'portfolio_collection' in globals() and portfolio_collection is not None:
        try:
            doc = portfolio_collection.find_one(sort=[('_id', -1)])
            if doc:
                doc['_id'] = str(doc['_id'])
                return doc
        except Exception as e:
            print(f"Error fetching portfolio: {e}")
            return None
    return None

@app.route('/health')
def health_check():
    """Health check endpoint for deployment monitoring"""
    try:
        # Test MongoDB connection
        if portfolio_collection is not None:
            portfolio_collection.find_one()
            db_status = "connected"
        else:
            db_status = "disconnected"
        
        return jsonify({
            'status': 'healthy',
            'database': db_status,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

@app.route('/')
def index():
    projects = get_projects_from_db()
    data = get_portfolio_from_db() or {}
    
    # Provide default structure to prevent template errors
    if not data.get('name'):
        data['name'] = 'Portfolio'
    if not data.get('title'):
        data['title'] = 'Web Developer & Designer'
    if not data.get('email'):
        data['email'] = 'contact@example.com'
    if not data.get('phone'):
        data['phone'] = '+1 (555) 000-0000'
    if not data.get('location'):
        data['location'] = 'Your Location'
    
    data['projects'] = projects
    return render_template('index.html', data=data)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.'
        })

@app.route('/api/projects')
def get_projects():
    """API endpoint to get all projects"""
    projects = get_projects_from_db()
    return jsonify(projects)

@app.route('/api/projects', methods=['POST'])
def add_project():
    """Add a new project"""
    if projects_collection is None:
        return jsonify({'success': False, 'message': 'Database not connected'}), 500
    
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['title', 'category', 'description', 'technologies']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'success': False, 'message': f'{field} is required'}), 400
        
        # Create project document
        project = {
            'title': data['title'],
            'category': data['category'],
            'description': data['description'],
            'technologies': data['technologies'],
            'image': data.get('image', '/static/images/project-placeholder.jpg'),
            'github_url': data.get('github_url', ''),
            'live_url': data.get('live_url', ''),
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        
        # Insert into database
        result = projects_collection.insert_one(project)
        
        return jsonify({
            'success': True, 
            'message': 'Project added successfully',
            'project_id': str(result.inserted_id)
        })
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error adding project: {str(e)}'}), 500

@app.route('/api/projects/<project_id>', methods=['PUT'])
def update_project(project_id):
    """Update an existing project"""
    if projects_collection is None:
        return jsonify({'success': False, 'message': 'Database not connected'}), 500
    
    try:
        data = request.get_json()
        
        # Validate ObjectId
        if not ObjectId.is_valid(project_id):
            return jsonify({'success': False, 'message': 'Invalid project ID'}), 400
        
        # Update project
        update_data = {
            'title': data.get('title'),
            'category': data.get('category'),
            'description': data.get('description'),
            'technologies': data.get('technologies'),
            'image': data.get('image'),
            'github_url': data.get('github_url'),
            'live_url': data.get('live_url'),
            'updated_at': datetime.now()
        }
        
        # Remove None values
        update_data = {k: v for k, v in update_data.items() if v is not None}
        
        result = projects_collection.update_one(
            {'_id': ObjectId(project_id)},
            {'$set': update_data}
        )
        
        if result.matched_count == 0:
            return jsonify({'success': False, 'message': 'Project not found'}), 404
        
        return jsonify({'success': True, 'message': 'Project updated successfully'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error updating project: {str(e)}'}), 500

@app.route('/api/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a project"""
    if projects_collection is None:
        return jsonify({'success': False, 'message': 'Database not connected'}), 500
    
    try:
        # Validate ObjectId
        if not ObjectId.is_valid(project_id):
            return jsonify({'success': False, 'message': 'Invalid project ID'}), 400
        
        result = projects_collection.delete_one({'_id': ObjectId(project_id)})
        
        if result.deleted_count == 0:
            return jsonify({'success': False, 'message': 'Project not found'}), 404
        
        return jsonify({'success': True, 'message': 'Project deleted successfully'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error deleting project: {str(e)}'}), 500

@app.route('/api/portfolio')
def get_portfolio_data():
    """API endpoint to get the full portfolio (including projects)."""
    data = get_portfolio_from_db()
    if not data:
        return jsonify({'success': False, 'message': 'Portfolio not found'}), 404
    data['projects'] = get_projects_from_db()
    return jsonify(data)


if __name__ == '__main__':
    # Production-ready configuration
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port) 