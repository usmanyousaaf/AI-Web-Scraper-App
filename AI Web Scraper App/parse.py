from groq import Groq

# Initialize Groq client with the API key directly
client = Groq(api_key="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")

# Define the template for parsing
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_groq(dom_chunks, parse_description, model="llama3-8b-8192"):
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        # Prepare the prompt
        prompt = template.format(dom_content=chunk, parse_description=parse_description)

        # Send prompt to Groq for processing, specifying the model
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model=model  # Specify the model
        )
        
        # Print status and store result
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response.choices[0].message.content)  # Access the content

    return "\n".join(parsed_results)
