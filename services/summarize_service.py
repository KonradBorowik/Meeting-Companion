def summarize_transcription(transcript, llm_chain):
    result = llm_chain.run(transcript)
    return result
