# Mental Health Documentation

Comprehensive mental health assessment tools, screening instruments, and support resources.

## Table of Contents

1. [Mental Health Assessment](#mental-health-assessment)
2. [Mental Health Chat](#mental-health-chat)
3. [SANE Interview](#sane-interview)
4. [Symptom Detection Chat](#symptom-detection-chat)
5. [Mental Health Reports](#mental-health-reports)
6. [Crisis Resources](#crisis-resources)

---

## Mental Health Assessment

Structured assessment tools for mental health screening and evaluation.

### Features
- Validated screening instruments
- Symptom severity assessment
- Risk stratification
- Diagnostic support
- Report generation
- Treatment recommendations

### Usage

#### Programmatic
```python
from medkit.mental_health.mental_health_assessment import assess_mental_health

# Conduct mental health assessment
responses = {
    "mood": "depressed",
    "sleep": "poor",
    "appetite": "decreased",
    "energy": "low"
}

assessment = assess_mental_health(responses)
print(f"Risk Level: {assessment.risk_level}")
print(f"Severity: {assessment.severity_score}")
print(f"Recommendations: {assessment.recommendations}")
```

#### Command-Line
```bash
python cli/cli_mental_health.py --assessment
```

### Screening Instruments

#### Depression Screening
- **PHQ-9 (Patient Health Questionnaire-9)**
  - 9-item depression severity scale
  - Scores 0-27 (none, mild, moderate, moderately severe, severe)
  - Questions about mood, sleep, appetite, guilt, energy

- **PHQ-2 (Quick Screen)**
  - 2-item screen for depression
  - Good sensitivity and specificity
  - Quick initial assessment

#### Anxiety Screening
- **GAD-7 (Generalized Anxiety Disorder-7)**
  - 7-item anxiety severity scale
  - Scores 0-21
  - Assess worry, panic, tension

- **STAI (State-Trait Anxiety Inventory)**
  - 40-item comprehensive anxiety assessment
  - Distinguishes state vs. trait anxiety

#### Substance Use
- **DAST-10 (Drug Abuse Screening Test)**
  - 10-item substance use screening
  - Good sensitivity for substance disorders

- **AUDIT (Alcohol Use Disorders Identification Test)**
  - 10-item alcohol screening
  - Identifies hazardous drinking patterns

#### Bipolar Disorder
- **Mood Disorder Questionnaire (MDQ)**
  - 13-item screening for bipolar disorder
  - Assesses hypomanic/manic symptoms

#### PTSD
- **PCL-5 (PTSD Checklist for DSM-5)**
  - 20-item PTSD symptom assessment
  - Validated trauma screening tool

### Assessment Components

#### Mood Assessment
- Current mood state
- Mood stability and variability
- Mood triggers
- Impact on functioning

#### Cognitive Assessment
- Concentration and attention
- Memory function
- Decision-making ability
- Suicidal/homicidal ideation

#### Sleep Assessment
- Sleep quantity (hours per night)
- Sleep quality
- Insomnia or hypersomnia
- Sleep disturbances

#### Appetite Assessment
- Changes in appetite
- Weight changes
- Eating pattern changes
- Nutritional status

#### Functional Assessment
- Work/school performance
- Social relationships
- Self-care activities
- Activities of interest

### Examples

```python
# Depression assessment
assessment = assess_mental_health({"mood": "depressed", "energy": "low"})

# Anxiety assessment
assessment = assess_mental_health({"worry": "constant", "panic": "frequent"})

# Comprehensive assessment
assessment = assess_mental_health({
    "mood": "variable",
    "sleep": "poor",
    "appetite": "decreased",
    "energy": "low",
    "concentration": "poor"
})
```

---

## Mental Health Chat

Conversational support and information interface.

### Features
- Chat-based interaction
- Empathetic responses
- Information provision
- Resource recommendations
- Crisis identification
- Appointment scheduling assistance

### Usage

#### Programmatic
```python
from medkit.mental_health.mental_health_chat import start_mental_health_chat

# Start chat session
chat = start_mental_health_chat(user_name="User")

# Single turn conversation
response = chat.send_message("I've been feeling really sad lately")
print(response)

# Continuous conversation
while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit']:
        break
    response = chat.send_message(user_input)
    print(f"Assistant: {response}")
```

#### Command-Line
```bash
python cli/cli_mental_health.py --chat
```

### Chat Capabilities
- **Emotional Support**: Validation and empathetic listening
- **Psychoeducation**: Information about mental health conditions
- **Coping Strategies**: Practical techniques and skills
- **Resource Connection**: Referrals and resource information
- **Crisis Assessment**: Identifies urgent needs

### Common Chat Topics
- Depression and low mood
- Anxiety and worry
- Sleep problems
- Relationship issues
- Work stress
- Grief and loss
- Life transitions
- Self-esteem concerns

### Safety Features
- **Crisis Detection**: Identifies suicidal/homicidal ideation
- **Emergency Response**: Provides crisis resources
- **Escalation Path**: Recommends professional help
- **Confidentiality**: Maintains privacy within system limitations

---

## SANE Interview

Structured Affective Neuroscience Environment interview protocol.

### Features
- Comprehensive psychiatric interview
- Structured questioning
- Symptom documentation
- Risk assessment
- Diagnostic formulation
- Treatment planning support

### Usage

#### Programmatic
```python
from medkit.mental_health.sane_interview import SANEInterview

# Initialize SANE interview
interview = SANEInterview(patient_name="John Doe")

# Conduct interview sections
demographics = interview.demographics_section()
chief_complaint = interview.chief_complaint_section()
present_illness = interview.present_illness_section()
past_psychiatric = interview.past_psychiatric_section()
substance_use = interview.substance_use_section()
medical_history = interview.medical_history_section()
family_history = interview.family_history_section()
social_history = interview.social_history_section()
mental_status = interview.mental_status_exam()

# Generate interview summary
summary = interview.generate_summary()
```

#### Command-Line
```bash
python cli/cli_mental_health.py --interview
```

### SANE Interview Components

#### Chief Complaint
- Primary reason for visit
- Timeline of symptom onset
- Acute vs. chronic presentation

#### History of Present Illness (HPI)
- Detailed symptom description
- Onset and progression
- Associated symptoms
- Trigger factors
- Previous episodes
- Treatment history

#### Past Psychiatric History
- Prior diagnoses
- Previous hospitalizations
- Medication trials
- Therapy history
- Suicide/self-harm attempts
- Violence history

#### Substance Use History
- Alcohol use
- Drug use (prescription and illicit)
- Tobacco use
- Caffeine use
- Age of first use
- Current use patterns
- Dependence symptoms

#### Medical History
- Chronic medical conditions
- Medications
- Allergies
- Surgeries
- Neurological history
- Head trauma

#### Family Psychiatric History
- Family members with mental illness
- Suicide in family
- Substance use in family
- Medical conditions

#### Social History
- Living situation
- Relationships
- Employment/school
- Legal issues
- Financial status
- Support systems

#### Mental Status Examination
- **Appearance**: Grooming, clothing, psychomotor activity
- **Behavior**: Cooperation, agitation, withdrawal
- **Speech**: Rate, volume, coherence
- **Mood & Affect**: Current mood, emotional expression
- **Thought Process**: Organization, flow
- **Thought Content**: Delusions, hallucinations, obsessions
- **Perception**: Auditory/visual hallucinations
- **Cognition**: Orientation, memory, concentration, intelligence
- **Judgment**: Decision-making ability
- **Insight**: Awareness of illness

---

## Symptom Detection Chat

AI-powered conversational symptom analysis for mental health.

### Features
- Conversational symptom gathering
- Symptom pattern recognition
- Preliminary diagnostic suggestions
- Red flag identification
- Resource recommendations
- Urgency assessment

### Usage

#### Programmatic
```python
from medkit.mental_health.sympton_detection_chat import SymptomDetectionChat

# Start symptom detection
detector = SymptomDetectionChat()

# Gather symptoms conversationally
symptoms = detector.gather_symptoms()

# Analyze and generate report
analysis = detector.analyze_gathered_symptoms()
print(f"Symptoms: {analysis.identified_symptoms}")
print(f"Likely Conditions: {analysis.possible_diagnoses}")
print(f"Urgency: {analysis.urgency_level}")
```

#### Command-Line
```bash
python cli/cli_symptoms_checker.py --symptoms "sadness,hopelessness,fatigue"
```

### Mental Health Symptoms Covered

#### Mood Symptoms
- Depression
- Mania
- Hypomania
- Mood instability
- Irritability
- Anxiety

#### Cognitive Symptoms
- Difficulty concentrating
- Memory problems
- Confusion
- Difficulty decision-making
- Intrusive thoughts

#### Sleep Symptoms
- Insomnia
- Hypersomnia
- Nightmares
- Sleep terror
- Restless sleep

#### Behavioral Symptoms
- Withdrawal from activities
- Reckless behavior
- Self-harm
- Aggression
- Increased/decreased activity

#### Physical Symptoms
- Fatigue
- Appetite changes
- Weight changes
- Aches and pains
- Restlessness

---

## Mental Health Reports

Generate comprehensive mental health reports and summaries.

### Features
- Report generation
- Treatment plans
- Medication recommendations
- Psychotherapy suggestions
- Follow-up scheduling
- Referral generation

### Usage

#### Programmatic
```python
from medkit.mental_health.mental_health_report import generate_mental_health_report

# Generate comprehensive report
assessment_data = {...}  # From assessment
report = generate_mental_health_report(assessment_data)

print(report.diagnosis)
print(report.severity_assessment)
print(report.treatment_plan)
print(report.recommended_follow_up)
```

### Report Components

#### Summary
- Patient demographics
- Chief complaint
- Timeline
- Symptoms

#### Assessment
- Diagnostic impression
- Severity rating
- Functional impact
- Risk assessment

#### Treatment Recommendations
- Medication options
- Psychotherapy modalities
- Lifestyle modifications
- Self-care strategies

#### Follow-Up
- Timing of next visit
- Monitoring parameters
- Crisis plan
- Resources

---

## Crisis Resources

Emergency contacts and crisis support information.

### ⚠️ EMERGENCY RESOURCES

#### Immediate Help
- **National Suicide Prevention Lifeline**: 988 (call or text, US)
- **Crisis Text Line**: Text HOME to 741741
- **International Association for Suicide Prevention**: https://www.iasp.info/resources/Crisis_Centres/

#### Emergency Services
- **Emergency Room**: Call 911 (US) or your local emergency number
- **Mobile Crisis Teams**: Available in many areas
- **Psychiatric Hospitals**: 24-hour inpatient care

#### Substance Use Help
- **SAMHSA National Helpline**: 1-800-662-4357 (free, confidential, 24/7)
- **Alcoholics Anonymous**: https://www.aa.org/
- **Narcotics Anonymous**: https://www.na.org/

#### General Mental Health Resources
- **Psychology Today Therapist Directory**: https://www.psychologytoday.com/
- **NAMI (National Alliance on Mental Illness)**: https://www.nami.org/
- **Mental Health America**: https://www.mhanational.org/

### Crisis Safety Planning
1. **Identify Warning Signs**: What leads to crisis
2. **Internal Coping Strategies**: Strategies to use alone
3. **External Coping Strategies**: Social support activities
4. **Social Contacts**: People to reach out to
5. **Professional Contacts**: Therapist, doctor, crisis line
6. **Hospitalization Plan**: When/where to go for emergency help

---

## Important Disclaimers

### This System is NOT for Emergencies
- **Not a substitute for emergency services**
- If in immediate danger, call 911
- If suicidal, contact 988 or crisis line immediately
- For serious mental health concerns, seek professional help

### Professional Mental Health Care
- This tool provides **information and support only**
- Cannot diagnose mental health conditions
- Cannot provide psychotherapy
- Cannot prescribe medications
- Assessment results require professional confirmation

### When to Seek Professional Help
- Symptoms lasting 2+ weeks
- Symptoms interfering with daily life
- Thoughts of self-harm or suicide
- Substance use problems
- Severe anxiety or panic
- Dramatic behavior changes
- Inability to care for yourself

---

## Related Documentation

- [Medical Reference Documentation](MEDICAL_REFERENCE.md)
- [Drug Database Documentation](DRUG_DATABASE.md)
- [Diagnostic Tools Documentation](DIAGNOSTIC_TOOLS.md)
- [CLI Tools Documentation](../cli/README.md)
- [API Reference](api/modules.rst)

---

## Disclaimer

This system is for **educational and informational purposes only**. It is not a substitute for professional mental health care, psychiatric evaluation, or emergency mental health services. Always consult with qualified mental health professionals for diagnosis, treatment, and emergency situations.

**If you are in crisis or having thoughts of self-harm, please contact:**
- National Suicide Prevention Lifeline: 988
- Crisis Text Line: Text HOME to 741741
- Emergency Services: 911
- Nearest Emergency Room
