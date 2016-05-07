import os

def sample_cf_cli_model(story_title):
    os.system("th sample.lua -checkpoint cv/model_cf_cli_stories.t7 -length 5000 -gpu -1 -temperature 0.6 -start_text \"<name>: {0}\" > tmp".format(story_title))
    return open('tmp', 'r').read()
