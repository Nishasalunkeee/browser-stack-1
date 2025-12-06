# BrowserStack Testathon Missions - All 4 Missions

## Overview

This directory contains documentation and resources for completing 4 out of 6 available missions for the BrowserStack Developers Day Testathon (FinStack RC v2.4.0-RC1).

## Missions Status

### ✅ Mission 2: Pixel-Perfect Guardian (Percy)
**Type:** Visual Regression Testing  
**Duration:** 30 minutes  
**Deliverable:** Percy Dashboard Build URL  

**What you'll do:**
1. Create Percy project for FinStack app
2. Capture baseline snapshot of login page
3. Click "Toggle Button" to change UI
4. Capture second snapshot
5. Review visual diffs (red highlights show changes)
6. Copy Percy build URL

**Key Link:** https://percy.io

---

### ✅ Mission 4: AI Self-Heal
**Type:** Self-Healing Automation  
**Duration:** 40 minutes  
**Deliverable:** Public Session URL with "Healed" badge  

**What you'll do:**
1. Record login test automation
2. Run it successfully (baseline)
3. Click "Toggle Button" to break selectors
4. Re-run with AI Self-Heal enabled
5. AI automatically fixes broken locators
6. Copy public session URL showing "Healed" badge

**Key Link:** https://app.browserstack.com/automate

---

### ✅ Mission 5: Inclusive Engineer (Accessibility)
**Type:** WCAG Compliance Audit  
**Duration:** 35 minutes  
**Deliverable:** Public Accessibility Report URL  

**Pages to scan:**
- Dashboard
- Login
- Transactions  
- Reports

**What you'll do:**
1. Run accessibility scan on all 4 pages
2. Use "High-Impact" audit level
3. Review findings:
   - Color contrast
   - Alt text
   - ARIA labels
   - Keyboard navigation
4. Copy public report URL

**Key Link:** https://www.browserstack.com/accessibility

---

### ✅ Mission 1: AI Test Management
**Type:** Test Case Generation & Automation  
**Duration:** 45 minutes  
**Deliverables:** CSV + Build URL  

**What you'll do:**
1. Use AI to generate test cases from user stories
2. Generate 8-12 test cases
3. Convert 2 to automated scripts:
   - Login Test
   - EMI Calculator Test
4. Execute tests on BrowserStack
5. Export test cases to CSV
6. Copy Low-Code build URL

**Key Link:** https://app.browserstack.com/test-management

---

## Total Deliverables

| Mission | Deliverable |
|---------|-------------|
| M2 | Percy Build URL |
| M4 | Self-Heal Session URL |
| M5 | Accessibility Report URL |
| M1 | test_cases.csv + Build URL |

## Execution Order

1. **Start with M2** (Percy) - Easiest, 30 min
2. **Then M4** (Self-Heal) - 40 min
3. **Then M5** (Accessibility) - 35 min
4. **Finally M1** (Test Management) - 45 min

**Total Time:** ~2.5 hours

## Folder Structure

```
missions/
├── README.md (this file)
├── mission-1-ai-test-management/
│   └── README.md
├── mission-2-percy/
│   └── README.md (to be added)
├── mission-4-ai-self-heal/
│   └── README.md (to be added)
└── mission-5-accessibility/
    └── README.md (to be added)
```

## Next Steps

1. Read SUBMISSION.md for detailed instructions
2. Execute missions in recommended order
3. Collect all URLs and CSV file
4. Email Squad Lead with:
   - GitHub repo link
   - All 4 mission URLs
   - test_cases.csv file

## Success Criteria

- [ ] All 4 mission URLs collected
- [ ] test_cases.csv exported
- [ ] All URLs are public and accessible
- [ ] GitHub repo is public
- [ ] Submission email sent to Squad Lead

---

**Project:** FinStack RC v2.4.0-RC1 Testing  
**Event:** BrowserStack Developers Day Testathon  
**Last Updated:** December 6, 2025
