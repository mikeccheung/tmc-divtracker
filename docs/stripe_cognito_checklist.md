# Stripe & Cognito Setup Checklist

## AWS Cognito (Google SSO)

1. **Create User Pool**
   - Navigate to Cognito → *Create user pool*.
   - Choose *Federated identity providers* with Google.
   - Configure hosted UI domain and callback URLs (e.g., `https://app.example.com/auth/callback`).

2. **Configure Google Identity Provider**
   - Obtain client ID/secret from Google Cloud Console (OAuth consent screen set to External).
   - Add authorized redirect URI pointing to Cognito hosted UI callback.

3. **App Client & Settings**
   - Create a user pool app client without client secret (for public web app).
   - Enable OAuth 2.0 flows: Authorization code grant, Implicit grant (optional).
   - Select scopes: `email`, `openid`, `profile`.
   - Configure CORS and allowed origins for local dev (`http://localhost:3000`).

4. **Domain & Certificates**
   - Assign a Cognito hosted domain or custom domain with ACM certificate.

5. **Token Verification**
   - Export user pool ID, region, and app client ID for backend verification.

## Stripe Subscriptions

1. **Create Stripe Account & Products**
   - Define pricing for Free (no Stripe), Pro (`price_pro_monthly`/`price_pro_yearly`), and Plus tiers.

2. **Configure Webhooks**
   - Create endpoint (e.g., `/api/v1/billing/stripe/webhook`).
   - Listen to `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted` events.
   - Store signing secret securely in backend environment variables.

3. **Stripe Customer Portal**
   - Enable the billing portal for self-serve plan management.
   - Save the portal configuration ID for backend usage.

4. **Stripe Checkout Session Flow**
   - Implement backend endpoint to create Checkout Sessions with success/cancel URLs.
   - Attach Cognito user ID/email to `customer_email` for new users or `customer` for existing.

5. **Environment Variables**
   - `STRIPE_API_KEY`
   - `STRIPE_WEBHOOK_SECRET`
   - `STRIPE_PRICE_PRO_MONTHLY`
   - `STRIPE_PRICE_PRO_YEARLY`
   - `STRIPE_PRICE_PLUS_MONTHLY`
   - `STRIPE_PRICE_PLUS_YEARLY`

6. **Test Mode Validation**
   - Use Stripe CLI or dashboard to trigger test webhooks.
   - Confirm subscription status updates in the database.

7. **Production Launch Checklist**
   - Replace test keys with live keys.
   - Update domain URLs for Checkout success/cancel.
   - Enable email notifications for payment failures and upcoming renewals.
