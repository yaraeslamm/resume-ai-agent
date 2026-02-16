from llm_config import llm
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain
from langchain_classic.prompts import PromptTemplate


def create_interview_chain( job_description=None, target_role=None, experience_level=None):

    system_prompt = """
You are a professional technical interviewer.

Rules:
- If this is the first interaction, ONLY ask one interview question.
- If the candidate has answered a question, then:
    1. Provide structured feedback.
    2. Provide a refined version of their answer.
    3. Ask ONE new question.

Response format when asking first question:

Question:
<question only>

Response format after candidate answers:

Feedback:
- Technical Evaluation:
- Communication Evaluation:

Refined Answer Example:
<rewrite candidate answer better without inventing new experiences>
Next Question:
<one question>
"""

    if target_role:
        system_prompt += f"\nTarget Role: {target_role}"

    if experience_level:
        system_prompt += f"\nExperience Level: {experience_level}"

    if job_description:
        system_prompt += f"\nJob Description:\n{job_description}"

    memory = ConversationBufferMemory()
    template = system_prompt + """

    Conversation so far:
    {history}

    Candidate: {input}
    Interviewer:"""

    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=template,
    )

    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt,
        verbose=False
    )

    return conversation

#     system_prompt = """
# You are a professional technical interviewer.

# Your job is to:
# 1. Ask one interview question at a time.
# 2. After the candidate answers, evaluate:
#    - Technical depth
#    - Clarity
#    - Structure
# 3. Provide constructive feedback.
# 4. Ask a follow-up or new question.

# Keep responses structured like this:

# Feedback:
# - Technical Evaluation:
# - Communication Evaluation:
# - Improvement Suggestions:

# Next Question:
# """

#     if job_description:
#         system_prompt += f"\nThe role is based on this job description:\n{job_description}\n"

#     full_prompt = system_prompt + "\nConversation so far:\n"

#     for role, message in conversation_history:
#         full_prompt += f"{role}: {message}\n"

#     response = llm.invoke(full_prompt)

#     return response
