"""
Module Documentation: api_methods.py

This module contains various methods to handle Tigrinya characters, including retrieving their variations, English representations, and audio pronunciations.

Functions:
1. get_character_variations: Retrieves all variations of Tigrinya characters.
2. get_variations: Retrieves all variations of a specific Tigrinya character.
3. get_english_representation: Retrieves the English representation of a specific Tigrinya character.
4. get_audio_pronunciations: Retrieves all audio pronunciations of Tigrinya characters.
5. get_audio_pronunciation: Retrieves the file path to the audio pronunciation of a specific Tigrinya character.

Constants:
- TIGRINYA_CHARACTERS: List of Tigrinya characters.
- ENG_REPRESENTATION: List of English representations for the Tigrinya characters.
- CH_VARIATION: List of variations for each Tigrinya character.
- CH_VARIATION_ENG_REP: English representations for the Tigrinya character variations.

Usage:
- Import this module to access the functions and constants for handling Tigrinya characters within the application.
- Call the appropriate function based on the specific requirement, such as retrieving variations, English representations, or audio pronunciations of Tigrinya characters.
"""

import os

# List of Tigrinya characters
TIGRINYA_CHARACTERS = ['ሀ','ለ','ሐ','መ','ረ','ሰ','ሸ','ቀ',
                    'ቐ','በ','ተ','ቸ','ነ','ኘ','አ','ከ',
                    'ኸ','ወ','ዐ','ዘ','ዠ','የ','ደ','ጀ',
                    'ገ','ጠ','ጨ','ጰ','ፀ','ፈ','ፐ','ቨ']

# List of English representations for the Tigrinya characters
ENG_REPRESENTATION = ['He', 'Le', 'Hhe', 'Me', 'Re', 'Se', 'She', 'Qe',
                    'Qqe', 'Be', 'Te', 'Che', 'Ne', 'Gne', 'Eh', 'Ke',
                    'Khe', 'We', 'EEh', 'Ze', 'Zhe', 'Ye', 'De', 'Je',
                    'Ge', 'Tte', 'Cche', 'Ppe', 'Tse', 'Fe', 'Pe', 'Ve']

# List of variations for each Tigrinya character
CH_VARIATION = [['ሀ','ሁ','ሂ','ሃ','ሄ','ህ','ሆ'], ['ለ','ሉ','ሊ','ላ','ሌ','ል','ሎ'],
                ['ሐ','ሑ','ሒ','ሓ','ሔ','ሕ','ሖ'], ['መ','ሙ','ሚ','ማ','ሜ','ም','ሞ'],
                ['ረ','ሩ','ሪ','ራ','ሬ','ር','ሮ'], ['ሰ','ሱ','ሲ','ሳ','ሴ','ስ','ሶ'],
                ['ሸ','ሹ','ሺ','ሻ','ሼ','ሽ','ሾ'], ['ቀ','ቁ','ቂ','ቃ','ቄ','ቅ','ቆ'],
                ['ቐ','ቑ','ቒ','ቓ','ቔ','ቕ','ቖ'], ['በ','ቡ','ቢ','ባ','ቤ','ብ','ቦ'],
                ['ተ','ቱ','ቲ','ታ','ቴ','ት','ቶ'], ['ቸ','ቹ','ቺ','ቻ','ቼ','ች','ቾ'],
                ['ነ','ኑ','ኒ','ና','ኔ','ን','ኖ'], ['ኘ','ኙ','ኚ','ኛ','ኜ','ኝ','ኞ'],
                ['አ','ኡ','ኢ','ኣ','ኤ','እ','ኦ'], ['ከ','ኩ','ኪ','ካ','ኬ','ክ','ኮ'],
                ['ኸ','ኹ','ኺ','ኻ','ኼ','ኽ','ኾ'], ['ወ','ዉ','ዊ','ዋ','ዌ','ው','ዎ'],
                ['ዐ','ዑ','ዒ','ዓ','ዔ','ዕ','ዖ'], ['ዘ','ዙ','ዚ','ዛ','ዜ','ዝ','ዞ'],
                ['ዠ','ዡ','ዢ','ዣ','ዤ','ዥ','ዦ'], ['የ','ዩ','ዪ','ያ','ዬ','ይ','ዮ'],
                ['ደ','ዱ','ዲ','ዳ','ዴ','ድ','ዶ'], ['ጀ','ጁ','ጂ','ጃ','ጄ','ጅ','ጆ'],
                ['ገ','ጉ','ጊ','ጋ','ጌ','ግ','ጎ'], ['ጠ','ጡ','ጢ','ጣ','ጤ','ጥ','ጦ'],
                ['ጨ','ጩ','ጪ','ጫ','ጬ','ጭ','ጮ'], ['ጰ','ጱ','ጲ','ጳ','ጴ','ጵ','ጶ'],
                ['ፀ','ፁ','ፂ','ፃ','ፄ','ፅ','ፆ'], ['ፈ','ፉ','ፊ','ፋ','ፌ','ፍ','ፎ'],
                ['ፐ','ፑ','ፒ','ፓ','ፔ','ፕ','ፖ'], ['ቨ','ቩ','ቪ','ቫ','ቬ','ቭ','ቮ']]

# English representations for the Tigrinya characters
CH_VARIATION_ENG_REP = [['He','Hu','Hi','Ha','Hie','H','Ho'], ['Le','Lu','Li','La','Lie','L','Lo'],
                        ['Hhe','Hhu','Hhi','Hha','Hhie','Hh','Hho'], ['Me','Mu','Mi','Ma','Mie','M','Mo'],
                        ['Re','Ru','Ri','Ra','Rie','R','Ro'], ['Se','Su','Si','Sa','Sie','S','So'],
                        ['She','Shu','Shi','Sha','Shie','Sh','Sho'], ['Qe','Qu','Qi','Qa','Qie','Q','Qo'],
                        ['Qqe','Qqu','Qqi','Qqa','Qqie','Qq','Qqo'], ['Be','Bu','Bi','Ba','Bie','B','Bo'],
                        ['Te','Tu','Ti','Ta','Tie','T','To'], ['Che','Chu','Chi','Cha','Chie','Ch','Cho'],
                        ['Ne','Nu','Ni','Na','Nie','N','No'], ['Gne','Gnu','Gni','Gna','Gnie','Gn','Gno'],
                        ['Eh','U','I','A','IE','E','O'], ['Ke','Ku','Ki','Ka','Kie','K','Ko'],
                        ['Khe','Khu','Khi','Kha','Khie','Kh','Kho'], ['We','Wu','Wi','Wa','Wie','W','Wo'],
                        ['EEh','UU','II','AA','IIE','EE','OO'], ['Ze','Zu','Zi','Za','Zie','Z','Zo'],
                        ['Zhe','Zhu','Zhi','Zha','Zhie','Zh','Zho'], ['Ye','Yu','Yi','Ya','Yie','Y','Yo'],
                        ['De','Du','Di','Da','Die','D','Do'], ['Je','Ju','Ji','Ja','Jie','J','Jo'],
                        ['Ge','Gu','Gi','Ga','Gie','G','Go'], ['Tte','Ttu','Tti','Tta','Ttie','Tt','Tto'],
                        ['Cche','Cchu','Cchi','Ccha','Cchie','Cch','Ccho'], ['Ppe','Ppu','Ppi','Ppa','Ppie','Pp','Ppo'],
                        ['Tse','Tsu','Tsi','Tsa','Tsie','Ts','Tso'], ['Fe','Fu','Fi','Fa','Fie','F','Fo'],
                        ['Pe','Pu','Pi','Pa','Pie','P','Po'], ['Ve','Vu','Vi','Va','Vie','V','Vo']]


def get_character_variations():
    """
    Retrieves all variations of Tigrinya characters.
    
    Returns:
        dict: A dictionary containing all variations of Tigrinya characters.
    """
    variations = {}
    for char in TIGRINYA_CHARACTERS:
        variations[char] = get_variations(char)
    return variations

def get_variations(character):
    """
    Retrieves all variations of a specific Tigrinya character.
    
    Args:
        character (str): The Tigrinya character.
        
    Returns:
        list: A list containing all variations of the Tigrinya character.
    """
    return CH_VARIATION[TIGRINYA_CHARACTERS.index(character)]

def get_english_representation(character):
    """
    Retrieves the English representation of a specific Tigrinya character.
    
    Args:
        character (str): The Tigrinya character.
        
    Returns:
        str: The English representation of the Tigrinya character.
    """
    found = False
    for char_list in CH_VARIATION:
        for c in char_list:
            if character == c:
                found = True
                va_idx = CH_VARIATION.index(char_list)
                ch_idx = char_list.index(character)
                break
            
    if found:
        return CH_VARIATION_ENG_REP[va_idx][ch_idx]
    else:
        return None

def get_audio_pronunciations():
    """
    Retrieves all audio pronunciations of Tigrinya characters.
    
    Returns:
        dict: A dictionary containing all audio pronunciations of Tigrinya characters.
    """
    AUDIO_PRONUNCIATIONS = {}
    for char_list in CH_VARIATION:
        for char in char_list:
            AUDIO_PRONUNCIATIONS[char] = get_audio_pronunciation(char)
    return AUDIO_PRONUNCIATIONS

def get_audio_pronunciation(character):
    """
    Retrieves the audio pronunciation of a specific Tigrinya character.
    
    Args:
        character (str): The Tigrinya character.
        
    Returns:
        str: The file path to the audio pronunciation of the Tigrinya character.
    """
    filename = get_english_representation(character)
    audio_file_path = os.path.join(os.path.dirname(__file__), '../', 'static', 'sounds', filename + '.wav')
    return audio_file_path
    #return os.path.join('static', 'sounds', filename + '.wav')
