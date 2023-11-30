browser_name = 'chrome'

# result = None

if (browser_name == 'chrome' or browser_name == 'firefox' or browser_name == 'opera' or browser_name == 'safari'
        or browser_name == 'edge'):
    if browser_name == 'chrome':
        result = f'{browser_name.capitalize()} Browser is selected'
    elif browser_name == 'firefox':
        result = f'{browser_name.capitalize()} Browser is selected'
    elif browser_name == 'opera':
        result = f'{browser_name.capitalize()} Browser is selected'
    elif browser_name == 'safari':
        result = f'{browser_name.capitalize()} Browser is selected'
    else:
        result = f'{browser_name.capitalize()} Browser is selected'
else:
    result = 'Invalid Browser Name'

print(result)
