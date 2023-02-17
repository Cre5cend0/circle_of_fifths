from mac_voice_assistant.AI import Assistant

if __name__ == '__main__':
    mac = Assistant('intents.json', model_name='mac')
    mappings = {}
    # Required methods ##Do not remove
    mac.set_intent_methods(mappings)
    mac.train_model()
    mac.save_model()
    mac.load_model()
    mac.assist()
