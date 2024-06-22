# xtts

# XTTS Custom Component for Home Assistant

_Originally forked from https://github.com/sfortis/openai_tts_

This component was originally forked from the original openai_tts to swap over to use the [XTTS-API-Server](https://github.com/daswer123/xtts-api-server)

This is still a work in progress, but essentially you simply set your host, the speaker, and eventually language too (right now hardcoded to "en"), and it will call out to your XTTS server when making the request.

## Description

The primary use case is to add this to your existing virtual assistant to use your own voices at home. This can be used in automations, assistants, scripts, or any other component that supports TTS within Home Assistant.

You **must** be running your own local instance of [XTTS-API-Server](https://github.com/daswer123/xtts-api-server).

## Features

- Text-to-Speech conversion using XTTS-Api-Server

## HACS installation ( _preferred!_ )

1. Go to the sidebar HACS menu

2. Click on the 3-dot overflow menu in the upper right and select the "Custom Repositories" item.

3. Copy/paste https://github.com/daswer123/xtts-api-server into the "Repository" textbox and select "Integration" for the category entry.

4. Click on "Add" to add the custom repository.

5. You can then click on the "OpenAI TTS Speech Services" repository entry and download it. Restart Home Assistant to apply the component.

6. Add the integration via UI, provide API key and select required model and voice. Multiple instances may be configured.

## Manual installation

1. Ensure you have a `custom_components` folder within your Home Assistant configuration directory.

2. Inside the `custom_components` folder, create a new folder named `xtts`.

3. Place the repo files inside `xtts` folder.

4. Restart Home Assistant

5. Add the integration via UI, provide API key and select required model and voice. Multiple instances may be configured.
