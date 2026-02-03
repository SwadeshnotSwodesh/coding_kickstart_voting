# Django Voting App - Render.com Deployment Guide

## Why Render.com?
✅ **Completely Free** - No credit card required
✅ **Auto-deploys** from GitHub
✅ **Includes Free PostgreSQL** database (5GB)
✅ **Perfect for Events** - Ready for production use
✅ **Easy Setup** - Just 5 minutes

## Deployment Steps

### Step 1: Push Code to GitHub

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### Step 2: Create Render.com Account

1. Go to [Render.com](https://render.com)
2. Sign up (use GitHub for easy login)
3. Verify your email

### Step 3: Create New Web Service

1. Click **New +** → **Web Service**
2. Click **Deploy an existing repo**
3. Choose your GitHub repository (voting app)
4. Click **Connect**

### Step 4: Configure Deployment

**Service Name**: `voting-app`

**Environment**: `Python 3`

**Build Command**:
```
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

**Start Command**:
```
gunicorn mysite.wsgi
```

**Plan**: `Free`

### Step 5: Add Environment Variables

Click **Environment** and add:

| Key | Value |
|-----|-------|
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `*.onrender.com` |
| `PYTHON_VERSION` | `3.11.0` |

(Render will auto-generate `SECRET_KEY` and `DATABASE_URL`)

### Step 6: Create PostgreSQL Database

1. Click **New +** → **PostgreSQL**
2. **Name**: `postgres-db`
3. **Plan**: `Free`
4. **Region**: Same as web service
5. Click **Create Database**

### Step 7: Connect Database

1. Copy the database connection string from PostgreSQL service
2. Add it as environment variable in your web service:
   - **Key**: `DATABASE_URL`
   - **Value**: (paste the connection string)

### Step 8: Deploy

Click **Create Web Service** and watch it deploy!

Your app will be available at: `https://voting-app-xxx.onrender.com`

## Post-Deployment

### Access Your App

- **Voting Page**: `https://voting-app-xxx.onrender.com/vote`
- **Admin Panel**: `https://voting-app-xxx.onrender.com/admin`

### Create Admin User

1. Go to Render Dashboard
2. Select your web service
3. Click **Shell** (top right)
4. Run:
   ```bash
   python manage.py createsuperuser
   ```

### Manage Your App

- **View Logs**: Click **Logs** tab
- **View Metrics**: Click **Metrics** tab
- **Restart**: Click **Restart** (near the top)

## Troubleshooting

### Application not loading

Check logs: **Logs** tab
```
Common issues:
- Migration failed → Run in Shell: python manage.py migrate
- Static files missing → Already handled by collectstatic
- Database error → Verify DATABASE_URL is set
```

### Database connection error

```bash
# SSH into service (via Shell)
python manage.py migrate
python manage.py createsuperuser
```

### Can't see voting interface

1. Ensure migrations ran successfully
2. Check **Logs** for errors
3. Restart the service
4. Try accessing `/admin` first to verify app is running

## Free Tier Limits

- **Compute**: 0.5 CPU, 512MB RAM (auto-sleeps after 15 min inactivity)
- **Storage**: 100GB (PostgreSQL 5GB)
- **Bandwidth**: Unlimited
- **Duration**: Unlimited (free forever)

**For your event**: Perfect! Users can vote without issues.

## Custom Domain (Optional)

1. Go to web service settings
2. Click **Custom Domains**
3. Add your domain
4. Update DNS records at your registrar
5. SSL certificate auto-configured

## Auto-Deployment

Every time you push to GitHub, Render automatically:
1. Builds your app
2. Runs migrations
3. Collects static files
4. Deploys to production

## Cost Monitoring

Render free tier: **$0/month**

No surprise charges! Free tier has no expiration.

## Before Event

### Checklist

- [ ] App deployed and accessible
- [ ] Database connected and working
- [ ] Admin account created
- [ ] Test the voting interface
- [ ] Share public link with participants
- [ ] Monitor logs during event
- [ ] Have backup plan (restart button ready)

### Test Voting Flow

1. Open `/vote` page
2. Enter name and vote
3. Verify votes are saved in admin panel
4. Test with multiple voters (simulate participants)

## Quick Links

- **Render Dashboard**: https://dashboard.render.com
- **Your App URL**: https://voting-app-xxx.onrender.com
- **Admin Panel**: https://voting-app-xxx.onrender.com/admin
- **Documentation**: https://render.com/docs

## Support During Event

If anything goes wrong:

1. **Check logs** - Usually shows the issue
2. **Restart service** - Click restart button
3. **Check database** - Verify PostgreSQL is running
4. **Clear cache** - Refresh page with Ctrl+Shift+Delete

**Your voting app is now live on the internet!** 🎉

Share the URL: `https://voting-app-xxx.onrender.com/vote`

Users can vote from any device, anywhere!
