# 🚀 Quick Deploy to Render - 5 Minutes!

## What You Need
1. GitHub account (free)
2. Render.com account (free)
3. Your code (ready!)

## Step-by-Step

### 1️⃣ Push to GitHub (2 min)
```bash
cd d:\Projects\MCC\kickstart_voting\coding_kickstart_voting
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### 2️⃣ Sign Up on Render (1 min)
- Go to https://render.com
- Click **Sign up**
- Use GitHub login (easiest)
- Verify email

### 3️⃣ Deploy on Render (2 min)

**A. Create Web Service**
- Click **New +** → **Web Service**
- Select your GitHub repository
- Click **Connect**

**B. Configure**
- Name: `voting-app`
- Environment: `Python 3`
- Build: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- Start: `gunicorn mysite.wsgi`
- Plan: `Free`

**C. Add Database**
- Click **New +** → **PostgreSQL**
- Name: `postgres-db`
- Plan: `Free`
- Create it

**D. Link Database**
- Copy PostgreSQL connection string
- Add to web service → Environment
- Key: `DATABASE_URL`
- Value: (paste the string)

**E. Deploy**
- Click **Create Web Service**
- Wait ~2 min for deployment

### 4️⃣ Setup Admin User

Once deployed:
1. Click web service → **Shell**
2. Run:
   ```bash
   python manage.py createsuperuser
   ```
3. Enter username, email, password

### 5️⃣ Done! 🎉

Your app is now live!
- **Vote**: `https://voting-app-xxx.onrender.com/vote`
- **Admin**: `https://voting-app-xxx.onrender.com/admin`

## That's It!

Share the voting link with your participants. They can vote from any device!

---

**Need Help?**
- See full guide: `RENDER_DEPLOYMENT.md`
- Check logs in Render dashboard
- Database included for free
- No credit card needed
- Completely free forever
