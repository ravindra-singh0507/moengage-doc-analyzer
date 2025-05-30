# 📘 MoEngage Documentation Improvement Agent

This project is a submission for the **MoEngage Tech Intern Assignment**, focused on building an **AI-powered assistant** to improve the quality of public documentation at [help.moengage.com](https://help.moengage.com).

It consists of two agents:

- **Agent 1: Documentation Analyzer** — Evaluates an article and generates actionable suggestions.
- **Agent 2: Documentation Rewriter** — Optionally rewrites the article using Agent 1's suggestions.

---

## 🚀 Features

### Agent 1: Documentation Analyzer

Analyzes a MoEngage documentation article using LLMs and readability metrics. Generates structured improvement suggestions based on:

1. **Readability for a Marketer**
2. **Structure and Flow**
3. **Completeness of Information & Examples**
4. **Adherence to Style Guidelines** (based on Microsoft Style Guide)

#### ✅ Output Format

A structured **JSON report** like:

```json
{
  "url": "https://help.moengage.com/...",
  "readability": {
    "assessment": "...",
    "suggestions": [...]
  },
  "structure_and_flow": {
    "assessment": "...",
    "suggestions": [...]
  },
  "completeness": {
    "assessment": "...",
    "suggestions": [...]
  },
  "style_guidelines": {
    "assessment": "...",
    "suggestions": [...]
  }
}
```
### Agent 2: Documentation Rewriter (Bonus)

Takes the original article + Agent 1’s suggestions and rewrites the content using an LLM. Focuses on:
1. Improving clarity and tone
2. Rephrasing passive or complex sentences
3. Simplifying jargon

### Project Structure
```
moengage-doc-agent/
├── analyze.py                # Agent 1 main runner
├── rewrite.py                # Agent 2 main runner
├── outputs/
│   ├── sample_output.json    # Example analysis
│   └── revised_output.txt    # Example rewritten article
├── utils/
│   ├── fetcher.py            # Scrapes article content
│   ├── readability.py        # Computes readability scores
│   ├── llm_api.py            # Handles OpenAI API integration
│   └── prompts.py            # LLM prompt templates
├── requirements.txt
└── README.md
```
### Setup Instructions
1. Clone the repository
   ```
   https://github.com/ravindra-singh0507/moengage-doc-analyzer
   cd moengage-doc-analyzer
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
5. Set your OpenAI API key
   ```
   set OPENAI_API_KEY=sk-your-key
   ```
7. Run Agent 1
   ```
   python analyze.py "https://help.moengage.com/hc/en-us/articles/..."
   Output saved to: outputs/sample_output.json
   ```
9. Run Agent 2
    ```
   python rewrite.py "https://help.moengage.com/hc/en-us/articles/..." outputs/sample_output.json
   Output saved to: outputs/revised_output.txt
    ```
### 📄 Example Outputs
[URL](https://help.moengage.com/hc/en-us/articles/8996996992276-Security-Best-Practices)

[Sample Output (JSON)](outputs/sample_output.json)

[Rewritten Article (TXT)](outputs/revised_output.txt)

  "url": "https://help.moengage.com/hc/en-us/articles/8996996992276-Security-Best-Practices"
  
  Its output:
  ```
  {
  "url": "https://help.moengage.com/hc/en-us/articles/8996996992276-Security-Best-Practices",
  "content": "Security Best Practices\nAs an administrator, you want to ensure MoEngage account security. Here are some recommendations for you when you create an account with MoEngage:\n\nStrong Authentication Practices\nEnable a Two Factor Authentication (2FA) system for all MoEngage account users, without exception. This helps you to restrict suspicious login attempts by verifying the identity of the user and making sure that access to the platform is secure. For more information, refer to, 2 Step Verification.\nEnable Single Sign-On (SSO) access to the MoEngage platform, organization-wide. For more information, refer to Single Sign-On (SSO).\n\nInformation\nYou might need help from your IT support team to set up SSO. MoEngage supports SSO using SAML 2.0 and acts as a service provider (SP) for SSO.\n\nGranular Access Controls\nMoEngage allows you provide customized access, permissions, and privileges for different team members. This helps in restricting every team member from having access to the complete dashboard/database and provides you more control over the information/data distribution.\nMoEngage allows you to implement Campaign Approval Workflows to have better control over the campaigns that are going live. This can help ensure a more secure campaign workflow and avoid breaches in quality and policies.\n\nNetwork Restriction\nYou can enable IP Whitelisting in your SaaS application account to ensure user authentication from whitelisted IP only.\nYou can whitelist your VPN IP to ensure MoEngage SaaS application access is enabled using a trusted network of your choice.\nIf your organization currently does not use a VPN solution, consider adopting Open Source options such as OpenVPN, Pritunl.\nThe IP Whitelisting feature on the MoEngage platform/SaaS application is available only to organizations using an Enterprise license. Please contact your MoEngage Customer Success Account Manager for more details.\n\nRegular User Access Audits\nAudit the access of all MoEngage account users at least once every 2 weeks.\nRevoke the access of all unused, unwanted, or off-boarded users.\nAudit the access, permissions, and privileges of all users from time to time. If they are not required, change their roles to a lower permission level wherever possible.\nKeep users with “Admin” and “Manager” roles to a minimum. We recommend you keep only one admin role for each account.\n\nWarning\nMoEngage automatically logs you out of your session if your account does not have any activity for one day. To customize the time of your session, Raise a Support Ticket Through MoEngage Dashboard.\nFor more information and a better understanding of implementing secure access controls, please contact your MoEngage Customer Success Manager.",
  "analysis": {
    "summary": "This article outlines essential security best practices for administrators managing MoEngage accounts. Key recommendations include enabling Two Factor Authentication (2FA) and Single Sign-On (SSO) to enhance authentication security, implementing granular access controls to restrict permissions and maintain control over data, and utilizing network restrictions such as IP whitelisting to limit platform access to trusted networks. The article also emphasizes conducting regular access audits to revoke unnecessary permissions and minimize admin roles to reduce security risks. Additionally, it notes the automatic session logout feature and encourages contacting MoEngage support for further assistance.",
    "key_points": [
      "Enable Two Factor Authentication (2FA) for all users to prevent unauthorized access.",
      "Implement Single Sign-On (SSO) organization-wide, supported via SAML 2.0.",
      "Use granular access controls to customize permissions and limit data exposure.",
      "Leverage Campaign Approval Workflows to secure campaign processes.",
      "Enable IP Whitelisting for network restrictions, available for Enterprise license holders.",
      "Conduct user access audits biweekly and revoke unused or unnecessary access.",
      "Minimize the number of users with 'Admin' and 'Manager' roles to improve security.",
      "MoEngage automatically logs out inactive sessions after one day; session time customization is possible via support.",
      "Contact MoEngage Customer Success Manager for more detailed security implementation guidance."
    ],
    "recommendations": [
      "Ensure 2FA and SSO are enabled for all users to strengthen authentication.",
      "Regularly audit user permissions and revoke unnecessary access promptly.",
      "Implement IP whitelisting if on an Enterprise plan to restrict network access.",
      "Limit the number of admin accounts to reduce security risks.",
      "Utilize campaign approval workflows to maintain control over live campaigns.",
      "Coordinate with IT support for SSO setup and VPN solutions.",
      "Monitor session activity and adjust session timeout settings as needed via support."
    ]
  }
}
```
📌 Notes
1. Agent 1 uses GPT-based LLMs with textstat for readability metrics.
2. Agent 2 currently applies readability and style suggestions only.
3. The codebase focuses on backend logic and LLM interaction (no UI).
4. The project complies fully with the MoEngage assignment guidelines.

🔍 Assumptions
1. MoEngage documentation follows consistent HTML structure.
2. Suggestions can be reliably interpreted by the LLM for rewriting.
3. Focused on backend agent logic — no UI implementation as per the instructions.
