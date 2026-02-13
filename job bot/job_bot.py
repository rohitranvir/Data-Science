#!/usr/bin/env python3
"""
Job Monitoring Bot - FIXED VERSION
Handles Naukri RSS issues properly
"""

import hashlib
import sqlite3
import time
import smtplib
import requests
import logging
import xml.etree.ElementTree as ET
import re
import json
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
from urllib.parse import quote

# ==================== CONFIGURATION ====================
# ↓↓↓ ONLY CHANGE THESE EMAIL SETTINGS ↓↓↓
email_config = { "smtp_server": "smtp.gmail.com", # for gmail 
                "smtp_port": 587, 
                "email_from": "rohitranveer358@gmail.com", 
                "email_to": "rohitranveer358@gmail.com", 
                "password": "rxotqkcuunrflprh" # ← change this (not regular password!) }
# ↑↑↑ ONLY CHANGE THESE EMAIL SETTINGS ↑↑↑

# Job filters
JOB_ROLES = ["Data Analyst", "Data Scientist", "Machine Learning Engineer"]
EXPERIENCE_LEVELS = ["fresher", "0-1 years", "0–1 years", "0 to 1 years", "0-1", "0–1", "0 yrs", "1 yrs"]
LOCATIONS = ["india", "remote"]
REQUIRED_KEYWORDS = ["sql", "python", "machine learning", "html", "css", "js"]
EXCLUDE_KEYWORDS = ["senior", "lead", "manager"]

# Alternative job sources (Free APIs that actually work)
JOB_SOURCES = [
    {
        "name": "GitHub Jobs API",
        "url": "https://jobs.github.com/positions.json?description=python&location=remote",
        "type": "api",
        "parser": "parse_github_jobs"
    },
    {
        "name": "RemoteOK API",
        "url": "https://remoteok.io/api",
        "type": "api", 
        "parser": "parse_remoteok_jobs"
    },
    {
        "name": "Arbeitnow API",
        "url": "https://www.arbeitnow.com/api/job-board-api",
        "type": "api",
        "parser": "parse_arbeitnow_jobs"
    }
]

# ==================== MAIN BOT CLASS ====================
class JobMonitoringBot:
    def __init__(self):
        """Initialize the bot"""
        self.setup_logging()
        self.init_database()
        self.logger.info("=" * 60)
        self.logger.info("Job Monitoring Bot v2.0 (Fixed)")
        self.logger.info("=" * 60)
        self.logger.info(f"Email alerts to: {EMAIL_CONFIG['email_to']}")
        self.logger.info(f"Monitoring for: {', '.join(JOB_ROLES)}")
        self.logger.info(f"Experience: 0-1 years / Fresher")
        self.logger.info(f"Required skills: {', '.join(REQUIRED_KEYWORDS)}")
        
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('job_bot.log', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def init_database(self):
        """Initialize SQLite database"""
        self.conn = sqlite3.connect('job_monitor.db')
        self.cursor = self.conn.cursor()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY,
                title TEXT,
                company TEXT,
                location TEXT,
                description TEXT,
                url TEXT,
                source TEXT,
                posted_date TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS alerts_sent (
                job_id TEXT,
                alert_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (job_id) REFERENCES jobs(id)
            )
        ''')
        
        self.conn.commit()
    
    def generate_job_id(self, title, company, url):
        """Generate unique job ID"""
        text = f"{title}_{company}_{url}".lower().strip()
        return hashlib.md5(text.encode()).hexdigest()
    
    def is_job_processed(self, job_id):
        """Check if job already exists"""
        self.cursor.execute("SELECT 1 FROM jobs WHERE id = ?", (job_id,))
        return self.cursor.fetchone() is not None
    
    def save_job(self, job_data):
        """Save job to database"""
        try:
            self.cursor.execute('''
                INSERT OR IGNORE INTO jobs 
                (id, title, company, location, description, url, source, posted_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                job_data['id'],
                job_data['title'],
                job_data['company'],
                job_data['location'],
                job_data.get('description', ''),
                job_data['url'],
                job_data['source'],
                job_data.get('posted_date', datetime.now().strftime('%Y-%m-%d'))
            ))
            self.conn.commit()
            return True
        except Exception as e:
            self.logger.error(f"Error saving job: {e}")
            return False
    
    def mark_alert_sent(self, job_id):
        """Mark that alert was sent for this job"""
        try:
            self.cursor.execute(
                "INSERT INTO alerts_sent (job_id) VALUES (?)",
                (job_id,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    # ============ JOB PARSERS ============
    
    def fetch_github_jobs(self, source_config):
        """Fetch jobs from GitHub Jobs API"""
        jobs = []
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(source_config['url'], headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                
                for item in data:
                    # Only get recent jobs (last 7 days)
                    posted_date = item.get('created_at', '')
                    if '2026-01' not in posted_date:  # Only get recent jobs
                        continue
                    
                    job_id = self.generate_job_id(
                        item.get('title', ''),
                        item.get('company', ''),
                        item.get('url', '')
                    )
                    
                    job_data = {
                        'id': job_id,
                        'title': item.get('title', ''),
                        'company': item.get('company', ''),
                        'location': item.get('location', 'Remote'),
                        'description': item.get('description', ''),
                        'url': item.get('url', ''),
                        'source': source_config['name'],
                        'posted_date': posted_date,
                        'full_text': f"{item.get('title', '')} {item.get('description', '')}".lower()
                    }
                    
                    jobs.append(job_data)
            
            self.logger.info(f"GitHub Jobs: Found {len(jobs)} jobs")
            
        except Exception as e:
            self.logger.error(f"Error fetching GitHub jobs: {e}")
        
        return jobs
    
    def fetch_remoteok_jobs(self, source_config):
        """Fetch jobs from RemoteOK API"""
        jobs = []
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(source_config['url'], headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                
                # Skip first element (status info)
                if isinstance(data, list) and len(data) > 1:
                    for item in data[1:]:  # Skip first element
                        if not isinstance(item, dict):
                            continue
                        
                        # Check if job is recent (within 7 days)
                        date_posted = item.get('date', '')
                        
                        job_id = self.generate_job_id(
                            item.get('position', ''),
                            item.get('company', ''),
                            item.get('url', '')
                        )
                        
                        job_data = {
                            'id': job_id,
                            'title': item.get('position', ''),
                            'company': item.get('company', ''),
                            'location': 'Remote',
                            'description': item.get('description', ''),
                            'url': item.get('url', ''),
                            'source': source_config['name'],
                            'posted_date': date_posted,
                            'full_text': f"{item.get('position', '')} {item.get('description', '')}".lower()
                        }
                        
                        jobs.append(job_data)
            
            self.logger.info(f"RemoteOK: Found {len(jobs)} jobs")
            
        except Exception as e:
            self.logger.error(f"Error fetching RemoteOK jobs: {e}")
        
        return jobs
    
    def fetch_arbeitnow_jobs(self, source_config):
        """Fetch jobs from Arbeitnow API"""
        jobs = []
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(source_config['url'], headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                
                if 'data' in data and isinstance(data['data'], list):
                    for item in data['data']:
                        # Check if job is recent
                        created_at = item.get('created_at', '')
                        
                        job_id = self.generate_job_id(
                            item.get('title', ''),
                            item.get('company_name', ''),
                            item.get('url', '')
                        )
                        
                        job_data = {
                            'id': job_id,
                            'title': item.get('title', ''),
                            'company': item.get('company_name', ''),
                            'location': item.get('location', ''),
                            'description': item.get('description', ''),
                            'url': item.get('url', ''),
                            'source': source_config['name'],
                            'posted_date': created_at,
                            'full_text': f"{item.get('title', '')} {item.get('description', '')}".lower()
                        }
                        
                        jobs.append(job_data)
            
            self.logger.info(f"Arbeitnow: Found {len(jobs)} jobs")
            
        except Exception as e:
            self.logger.error(f"Error fetching Arbeitnow jobs: {e}")
        
        return jobs
    
    def fetch_jobs(self, source_config):
        """Fetch jobs from a source"""
        parser_name = source_config.get('parser', '')
        
        if parser_name == 'parse_github_jobs':
            return self.fetch_github_jobs(source_config)
        elif parser_name == 'parse_remoteok_jobs':
            return self.fetch_remoteok_jobs(source_config)
        elif parser_name == 'parse_arbeitnow_jobs':
            return self.fetch_arbeitnow_jobs(source_config)
        else:
            return []
    
    # ============ FILTERS ============
    
    def check_job_filters(self, job):
        """Check if job matches all filters"""
        
        title = job['title'].lower()
        full_text = job.get('full_text', '').lower()
        
        # 1. Check excluded keywords in title
        for exclude in EXCLUDE_KEYWORDS:
            if exclude in title:
                return False, f"Contains '{exclude}'"
        
        # 2. Check job role
        role_match = False
        for role in JOB_ROLES:
            if role.lower() in title or role.lower() in full_text:
                role_match = True
                break
        
        if not role_match:
            return False, "Not matching job role"
        
        # 3. Check experience in description
        exp_match = False
        job_desc = job.get('description', '').lower()
        
        # Check for fresher/entry level
        if any(word in job_desc for word in ['fresher', 'entry level', '0 experience', 'no experience']):
            exp_match = True
        else:
            # Check for 0-1 years patterns
            for exp in EXPERIENCE_LEVELS:
                if exp in job_desc:
                    exp_match = True
                    break
            
            # Check for numeric patterns
            if not exp_match:
                patterns = [r'(\d+)\s*-\s*(\d+)\s+years', r'(\d+)\s*to\s*(\d+)\s+years']
                for pattern in patterns:
                    match = re.search(pattern, job_desc)
                    if match:
                        try:
                            min_exp = int(match.group(1))
                            if min_exp <= 1:
                                exp_match = True
                                break
                        except:
                            pass
        
        if not exp_match:
            # For remote jobs, be slightly more lenient
            if 'remote' not in job['location'].lower():
                return False, "Experience > 1 year"
        
        # 4. Check location
        location = job['location'].lower()
        location_match = False
        
        if 'remote' in location:
            location_match = True
        elif any(loc in location for loc in ['india', 'indian', 'delhi', 'mumbai', 'bangalore', 'chennai', 'hyderabad', 'pune']):
            location_match = True
        else:
            # Check in description
            if any(loc in full_text for loc in LOCATIONS):
                location_match = True
        
        if not location_match:
            return False, "Location not in India/Remote"
        
        # 5. Check required keywords
        keyword_match = False
        search_text = f"{title} {full_text}"
        
        for keyword in REQUIRED_KEYWORDS:
            if keyword in search_text:
                keyword_match = True
                break
        
        if not keyword_match:
            return False, "Missing required skills"
        
        return True, "All filters passed"
    
    # ============ EMAIL ALERT ============
    
    def send_email_alert(self, job):
        """Send email alert"""
        try:
            # Create email
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f"🚨 Job Alert: {job['title'][:50]}..."
            msg['From'] = EMAIL_CONFIG['email_from']
            msg['To'] = EMAIL_CONFIG['email_to']
            
            # Clean description for email
            description = job.get('description', '')[:500].replace('<', '&lt;').replace('>', '&gt;')
            
            # Email content
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px; }}
                    .header {{ background: #4a6fa5; color: white; padding: 20px; border-radius: 10px 10px 0 0; }}
                    .content {{ background: #f9f9f9; padding: 20px; border: 1px solid #ddd; border-radius: 0 0 10px 10px; }}
                    .job-title {{ color: #2c3e50; font-size: 22px; margin-bottom: 10px; }}
                    .label {{ font-weight: bold; color: #555; width: 100px; display: inline-block; }}
                    .apply-btn {{ display: inline-block; background: #27ae60; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold; margin-top: 20px; }}
                    .skills {{ background: #e8f4fc; padding: 10px; border-radius: 5px; margin: 10px 0; }}
                    .footer {{ margin-top: 30px; text-align: center; color: #777; font-size: 12px; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h2>🚨 NEW JOB ALERT</h2>
                    <p>Matching your criteria for {job['title'].split()[0]} roles</p>
                </div>
                
                <div class="content">
                    <div class="job-title">{job['title']}</div>
                    
                    <div>
                        <span class="label">Company:</span> {job['company']}<br>
                        <span class="label">Location:</span> {job['location']}<br>
                        <span class="label">Source:</span> {job['source']}<br>
                        <span class="label">Posted:</span> {job.get('posted_date', 'Today')}
                    </div>
                    
                    <div class="skills">
                        <strong>✅ Matches your skills:</strong><br>
                        {', '.join([k for k in REQUIRED_KEYWORDS if k in job.get('full_text', '').lower()])}
                    </div>
                    
                    <div style="text-align: center;">
                        <a href="{job['url']}" class="apply-btn" target="_blank">📋 APPLY NOW</a>
                    </div>
                    
                    <div style="margin-top: 20px; font-size: 14px;">
                        <strong>Job Details:</strong><br>
                        {description}...
                    </div>
                </div>
                
                <div class="footer">
                    <p>This is an automated alert from Job Monitoring Bot</p>
                    <p>Alert sent: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                </div>
            </body>
            </html>
            """
            
            text = f"""
🚨 NEW JOB ALERT

Position: {job['title']}
Company: {job['company']}
Location: {job['location']}
Source: {job['source']}
Posted: {job.get('posted_date', 'Today')}

Apply here: {job['url']}

This job matches your criteria for fresher/0-1 year roles in Data fields.

Alert sent: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            """
            
            # Attach both versions
            part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')
            msg.attach(part1)
            msg.attach(part2)
            
            # Send email
            with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port']) as server:
                server.starttls()
                server.login(EMAIL_CONFIG['email_from'], EMAIL_CONFIG['password'])
                server.send_message(msg)
            
            self.logger.info(f"✅ Email sent: {job['title'][:30]}...")
            return True
            
        except smtplib.SMTPAuthenticationError:
            self.logger.error("❌ Email authentication failed!")
            return False
        except Exception as e:
            self.logger.error(f"❌ Email error: {e}")
            return False
    
    # ============ MAIN PROCESSING ============
    
    def process_all_sources(self):
        """Process all job sources"""
        self.logger.info("\n" + "="*60)
        self.logger.info(f"Starting job scan: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        all_jobs = []
        matched_jobs = []
        alerts_sent = 0
        
        # Process each source
        for source in JOB_SOURCES:
            try:
                self.logger.info(f"\n📡 Checking: {source['name']}")
                
                # Fetch jobs from this source
                jobs = self.fetch_jobs(source)
                self.logger.info(f"   Found: {len(jobs)} jobs")
                
                if not jobs:
                    continue
                
                # Process each job
                source_matched = 0
                for job in jobs:
                    # Check if already processed
                    if self.is_job_processed(job['id']):
                        continue
                    
                    # Save job to database
                    self.save_job(job)
                    
                    # Check filters
                    matches, reason = self.check_job_filters(job)
                    
                    if matches:
                        matched_jobs.append(job)
                        source_matched += 1
                        
                        # Check if alert already sent
                        self.cursor.execute(
                            "SELECT 1 FROM alerts_sent WHERE job_id = ?",
                            (job['id'],)
                        )
                        alert_sent = self.cursor.fetchone() is not None
                        
                        if not alert_sent:
                            # Send alert
                            if self.send_email_alert(job):
                                self.mark_alert_sent(job['id'])
                                alerts_sent += 1
                    
                    all_jobs.append(job)
                
                if source_matched > 0:
                    self.logger.info(f"   Matched: {source_matched} jobs")
                
                # Small delay between sources
                time.sleep(1)
                
            except Exception as e:
                self.logger.error(f"   Error with {source['name']}: {e}")
                continue
        
        # Summary
        self.logger.info("\n" + "="*60)
        self.logger.info(f"SCAN SUMMARY")
        self.logger.info(f"Total jobs found: {len(all_jobs)}")
        self.logger.info(f"Jobs matching filters: {len(matched_jobs)}")
        self.logger.info(f"New alerts sent: {alerts_sent}")
        
        # Show matched job titles
        if matched_jobs:
            self.logger.info("\nMatched Jobs:")
            for job in matched_jobs[:5]:  # Show first 5
                self.logger.info(f"  • {job['title'][:40]}... at {job['company'][:20]}")
            if len(matched_jobs) > 5:
                self.logger.info(f"  ... and {len(matched_jobs) - 5} more")
        
        self.logger.info("="*60 + "\n")
        
        return {
            'total': len(all_jobs),
            'matched': len(matched_jobs),
            'alerts': alerts_sent
        }
    
    def run_continuously(self, interval_minutes=60):
        """Run the bot continuously"""
        self.logger.info(f"🔔 Monitoring started (every {interval_minutes} minutes)")
        self.logger.info("Press Ctrl+C to stop\n")
        
        # Run immediately
        self.process_all_sources()
        
        # Schedule regular runs
        schedule.every(interval_minutes).minutes.do(self.process_all_sources)
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            self.logger.info("\n👋 Bot stopped by user")
        finally:
            self.conn.close()

# ==================== UTILITIES ====================
def test_email():
    """Test email configuration"""
    print("\n" + "="*50)
    print("Testing Email Configuration")
    print("="*50)
    
    if EMAIL_CONFIG['email_from'] == "YOUR_EMAIL@gmail.com":
        print("❌ ERROR: You must configure email in the script!")
        print("Edit EMAIL_CONFIG at the top of job_bot.py")
        return False
    
    try:
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['email_from'], EMAIL_CONFIG['password'])
        server.quit()
        print("✅ Email configuration is valid!")
        return True
    except Exception as e:
        print(f"❌ Email error: {e}")
        print("\nFor Gmail users:")
        print("1. Enable 2-factor authentication")
        print("2. Generate App Password: https://myaccount.google.com/apppasswords")
        print("3. Use that 16-char password (not your regular password)")
        return False

def show_stats():
    """Show database statistics"""
    try:
        conn = sqlite3.connect('job_monitor.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM jobs")
        total_jobs = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(DISTINCT job_id) FROM alerts_sent")
        total_alerts = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(DISTINCT source) FROM jobs")
        sources_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT source, COUNT(*) FROM jobs GROUP BY source ORDER BY COUNT(*) DESC")
        sources = cursor.fetchall()
        
        print("\n" + "="*50)
        print("JOB BOT STATISTICS")
        print("="*50)
        print(f"Total jobs tracked: {total_jobs}")
        print(f"Total alerts sent: {total_alerts}")
        print(f"Sources active: {sources_count}")
        print("\nJobs by source:")
        for source, count in sources:
            print(f"  {source}: {count}")
        print("="*50)
        
        conn.close()
    except:
        print("No statistics available yet")

# ==================== MAIN ====================
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Job Monitoring Bot v2.0')
    parser.add_argument('--test', action='store_true', help='Test email only')
    parser.add_argument('--once', action='store_true', help='Run once and exit')
    parser.add_argument('--stats', action='store_true', help='Show statistics')
    parser.add_argument('--interval', type=int, default=60, help='Check interval in minutes (default: 60)')
    
    args = parser.parse_args()
    
    if args.test:
        test_email()
    elif args.stats:
        show_stats()
    elif args.once:
        bot = JobMonitoringBot()
        bot.process_all_sources()
        show_stats()
    else:
        if not test_email():
            exit(1)
        bot = JobMonitoringBot()
        bot.run_continuously(interval_minutes=args.interval)