# 🚀 Deployment Guide - Voice Assistant App

## ✅ Prerequisites
- GitHub repository: https://github.com/Pavan-484/dtl
- OpenAI API Key from: https://platform.openai.com/api-keys

---

## 📦 **Step 1: Deploy Backend to Railway**

### Option A: Using Railway Dashboard (Recommended)

1. **Go to Railway**: https://railway.app/new

2. **Click "Deploy from GitHub repo"**
   - Sign in with GitHub
   - Select repository: `Pavan-484/dtl`
   - Click "Add variables"

3. **Configure Environment Variables:**
   ```
   OPENAI_API_KEY=sk-proj-your-actual-openai-key-here
   ```

4. **Configure Service Settings:**
   - **Root Directory**: `backend`
   - **Build Command**: (leave empty - auto-detected)
   - **Start Command**: `python3 app.py`

5. **Click "Deploy"**

6. **Get Your Backend URL:**
   - After deployment, click on your service
   - Copy the URL (e.g., `https://your-app.railway.app`)
   - **Save this URL - you'll need it for the frontend!**

### Option B: Using Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
cd backend
railway init

# Add environment variable
railway variables set OPENAI_API_KEY=sk-proj-your-key-here

# Deploy
railway up
```

---

## 🌐 **Step 2: Deploy Frontend to Vercel**

### Option A: Using Vercel Dashboard (Recommended)

1. **Go to Vercel**: https://vercel.com/new

2. **Import your GitHub repository:**
   - Select: `Pavan-484/dtl`
   - Framework: **Vite**
   - Root Directory: `./` (leave default)

3. **Configure Build Settings:**
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Install Command**: `npm install`

4. **Add Environment Variable:**
   ```
   Name: VITE_API_URL
   Value: https://your-backend.railway.app
   ```
   ⚠️ **IMPORTANT**: Replace with your actual Railway backend URL from Step 1!

5. **Click "Deploy"**

6. **Wait for deployment** (1-2 minutes)

7. **Your app is live!** 🎉
   - Vercel will provide a URL like: `https://dtl-xyz.vercel.app`

### Option B: Using Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

#Follow prompts:
# - Framework: Vite
# - Build Command: npm run build
# - Output Directory: dist

# Add environment variable
vercel env add VITE_API_URL
# Enter your Railway backend URL when prompted

# Redeploy with new environment variable
vercel --prod
```

---

## ✅ **Step 3: Verify Deployment**

1. **Open your Vercel URL**
2. **Click "Tap Screen to Start"**
3. **Try voice commands:**
   - *"Go to Form"*
   - *"Read Sign"*
   - *"Go to Map"*

4. **Check Browser Console** (F12):
   - Should see: `🔊 TTS Request (OpenAI): [message]`
   - Should NOT see CORS or 404 errors

---

## 🐛 **Troubleshooting**

### Frontend can't connect to backend
- ✅ Check Railway backend is running (visit backend URL directly)
- ✅ Verify `VITE_API_URL` environment variable in Vercel
- ✅ Make sure Railway URL doesn't have trailing slash
- ✅ Check CORS is enabled in backend (it should be)

### "OPENAI_API_KEY not configured" error
- ✅ Verify API key is set in Railway environment variables
- ✅ Restart Railway service after adding the key

### Audio not working
- ✅ Grant microphone permission when prompted
- ✅ Use HTTPS (Vercel provides this automatically)
- ✅ Check browser console for errors

### Backend not responding
- ✅ Check Railway logs: Dashboard → Service → Logs
- ✅ Verify port binding is working correctly
- ✅ Make sure all dependencies installed correctly

---

## 🔄 **Updating Your App**

### After making code changes:

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Your changes"
   git push origin main
   ```

2. **Vercel** will auto-deploy (frontend)
3. **Railway** will auto-deploy (backend)

---

## 💰 **Cost Estimate**

- **Vercel**: Free (Hobby plan)
- **Railway**: $5/month credit (Free tier available)
- **OpenAI API**: Pay-per-use
  - Whisper: ~$0.006 per minute
  - TTS: ~$15 per 1M characters
  - GPT-4o Vision: ~$0.005 per image

---

## 🎯 **Quick Checklist**

- [ ] Backend deployed to Railway
- [ ] `OPENAI_API_KEY` added to Railway
- [ ] Copied Railway backend URL
- [ ] Frontend deployed to Vercel
- [ ] `VITE_API_URL` added to Vercel with Railway URL
- [ ] Tested voice commands on production URL
- [ ] Microphone permission granted
- [ ] Audio announcements working

---

## 📞 **Need Help?**

- Railway Docs: https://docs.railway.app
- Vercel Docs: https://vercel.com/docs
- OpenAI API Docs: https://platform.openai.com/docs

---

**🎉 Congratulations! Your voice assistant is now live!**
