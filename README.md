# Random String Generator Plugin for MusicBrainz Picard

## Overview

The Random String Generator plugin provides a new scripting function to generate random strings of a specified length. This can be useful for adding unique identifiers or other randomized data to your metadata.

## Installation

1. Download the `random_string_generator.py` file.
2. Open MusicBrainz Picard.
3. Go to `Options` -> `Plugins`.
4. Click on `Install Plugin...`.
5. Select the downloaded `random_string_generator.py` file.
6. Enable the plugin in the list and restart Picard if necessary.

## Usage

The plugin adds a new scripting function `$random_string(length)` that generates a random string of the specified length.

### Example Script

```python
$set(random_id,$random_string(10))
```

This script sets a tag random_id to a random string of 10 characters.
