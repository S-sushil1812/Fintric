## Environment Variables & Configuration

### Overview

FINTRIC uses environment variables to manage sensitive credentials and API keys. These should **never be committed to version control**.

### Quick Setup

1. **Create a `.env` file** in the project root directory
2. **Copy the sample configuration** provided below
3. **Fill in your credentials** (see instructions for each variable)
4. **Keep `.env` in `.gitignore`** (already configured)

```bash
# Template for .env file
GOOGLE_API_KEY=your_api_key_here
GOOGLE_CLIENT_ID=your_client_id_here
GOOGLE_CLIENT_SECRET=your_client_secret_here
GOOGLE_REDIRECT_URI=http://localhost:8501
```

---

## Required Variables

### `GOOGLE_API_KEY`

**Purpose:** Enables AI-powered transaction categorization and chatbot features using Google Gemini.

**Status:** ⚠️ **Recommended** (app works without it, but AI features disabled)

**How to get it:**
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key to your `.env` file

**Example:**
```env
GOOGLE_API_KEY=AIzaSyDxX_xXxXxXxXxXxXxXxXxXxXxXxXxXxX
```

**Security Note:** This key is sensitive. Never share it or commit it to git.

---

## Optional Variables (For OAuth Authentication)

The following variables enable Google OAuth login. Without them, users can still authenticate using username/password.

### `GOOGLE_CLIENT_ID`

**Purpose:** OAuth application identifier for Google authentication.

**Status:** ❌ **Optional** (basic auth still works without it)

**When needed:** Only if you want to enable "Continue with Google" functionality.

**How to get it:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google+ API
4. Create OAuth 2.0 credentials (Web application)
5. Copy the Client ID

**Example:**
```env
GOOGLE_CLIENT_ID=your_client_id_here
```

---

### `GOOGLE_CLIENT_SECRET`

**Purpose:** OAuth secret key for secure server-to-server communication with Google.

**Status:** ❌ **Optional** (paired with `GOOGLE_CLIENT_ID`)

**When needed:** Always used together with `GOOGLE_CLIENT_ID`.

**How to get it:**
1. From the same OAuth credentials page as `GOOGLE_CLIENT_ID`
2. Copy the Client Secret

**Example:**
```env
GOOGLE_CLIENT_SECRET=your_client_secret_here
```

**⚠️ Critical Security Warning:** 
- **This is highly sensitive.** Treat it like a password.
- **Never** commit this to version control.
- **Never** share with untrusted parties.
- Consider using cloud platform secret management (AWS Secrets Manager, Azure Key Vault, etc.)

---

### `GOOGLE_REDIRECT_URI`

**Purpose:** Callback URL where Google redirects users after OAuth authentication.

**Status:** ❌ **Optional** (paired with `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`)

**When needed:** Only if using Google OAuth.

**Default value:** `http://localhost:8501` (automatically used if not set)

**Configuration by environment:**

- **Local Development:**
  ```env
  GOOGLE_REDIRECT_URI=http://localhost:8501
  ```

- **Streamlit Cloud Deployment:**
  ```env
  GOOGLE_REDIRECT_URI=https://your-app.streamlit.app
  ```

- **Custom Domain:**
  ```env
  GOOGLE_REDIRECT_URI=https://yourdomain.com
  ```

**Note:** Must match exactly what you configured in Google Cloud Console OAuth settings.

---

## Security Best Practices

### ✅ Do's

- ✅ Use `.env` files for **local development only**
- ✅ Add `.env` to `.gitignore` to prevent accidental commits
- ✅ Rotate credentials regularly
- ✅ Use cloud platform secret managers for production (AWS Secrets Manager, Azure Key Vault, Google Secret Manager, etc.)
- ✅ Limit API key permissions to only required scopes
- ✅ Monitor API usage for unusual activity

### ❌ Don'ts

- ❌ **Never** commit `.env` files to git
- ❌ **Never** hardcode credentials in source code
- ❌ **Never** share credentials via email or chat
- ❌ **Never** use overly permissive API key scopes
- ❌ **Never** reuse the same API key across multiple projects
- ❌ **Never** commit `.env.local` or `.env.production` files

---

## Configuration for Different Environments

### Local Development

**File:** `.env` (create locally, don't commit)

```env
GOOGLE_API_KEY=your_development_key
GOOGLE_CLIENT_ID=your_dev_client_id
GOOGLE_CLIENT_SECRET=your_dev_client_secret
GOOGLE_REDIRECT_URI=http://localhost:8501
```

### Streamlit Cloud

**Setup:** Configure secrets in Streamlit Cloud dashboard (Settings → Secrets)

```
GOOGLE_API_KEY = your_production_key
GOOGLE_CLIENT_ID = your_cloud_client_id
GOOGLE_CLIENT_SECRET = your_cloud_client_secret
GOOGLE_REDIRECT_URI = https://your-app.streamlit.app
```

### Docker/Self-Hosted

**Method 1: Environment variables**
```bash
docker run -e GOOGLE_API_KEY=xxx -e GOOGLE_CLIENT_ID=yyy fintric:latest
```

**Method 2: .env file** (mount to container)
```bash
docker run --env-file .env fintric:latest
```

### Heroku

**Command line:**
```bash
heroku config:set GOOGLE_API_KEY=xxx
heroku config:set GOOGLE_CLIENT_ID=yyy
heroku config:set GOOGLE_CLIENT_SECRET=zzz
heroku config:set GOOGLE_REDIRECT_URI=https://your-app.herokuapp.com
```

---

## Troubleshooting

### "GOOGLE_API_KEY not configured" Error

**Cause:** Environment variable not set.

**Solutions:**
- Add `GOOGLE_API_KEY` to your `.env` file
- Verify `.env` file exists in project root
- Restart the application
- For production, verify secret is set in your platform

### "Invalid OAuth credentials" Error

**Cause:** `GOOGLE_CLIENT_ID` or `GOOGLE_CLIENT_SECRET` is invalid.

**Solutions:**
- Verify credentials in Google Cloud Console
- Ensure `GOOGLE_REDIRECT_URI` matches exactly in Google Console settings
- Check for trailing spaces in credentials
- Regenerate credentials if necessary

### "Redirect URI mismatch" Error

**Cause:** `GOOGLE_REDIRECT_URI` doesn't match Google Cloud Console configuration.

**Solutions:**
- Check Google Cloud Console → APIs & Services → Credentials
- Ensure URI matches exactly (including protocol and domain)
- Add multiple URIs in console if supporting multiple environments

---

## Creating a `.env.example` File

Share this template with your team **without secrets**:

```env
# Google Gemini API - AI Features
# Get key at: https://makersuite.google.com/app/apikey
GOOGLE_API_KEY=your_api_key_here

# Google OAuth - Optional Social Login
# Get credentials at: https://console.cloud.google.com/
GOOGLE_CLIENT_ID=your_client_id_here
GOOGLE_CLIENT_SECRET=your_client_secret_here
GOOGLE_REDIRECT_URI=http://localhost:8501
```

**Instructions:**
1. Copy to `.env`: `cp .env.example .env`
2. Fill in your actual credentials
3. Keep `.env` private - never commit to git

---

## Minimal Setup (No OAuth)

If you only want basic authentication (no Google OAuth):

```env
# Only this is recommended
GOOGLE_API_KEY=your_api_key_here

# These are optional - app works without them
# GOOGLE_CLIENT_ID=
# GOOGLE_CLIENT_SECRET=
# GOOGLE_REDIRECT_URI=http://localhost:8501
```

---

## Full Production Setup

For production deployments with all features:

```env
GOOGLE_API_KEY=your_production_api_key
GOOGLE_CLIENT_ID=your_production_client_id
GOOGLE_CLIENT_SECRET=your_production_client_secret
GOOGLE_REDIRECT_URI=https://yourdomain.com
```

Store these in your platform's secret management service, **not** in a `.env` file.
