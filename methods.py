"""
Module Documentation: methods.py

This module contains functions related to the quiz functionality of the Tigrinya Alphabet Learning Web App.

Functions:
    - selected_characters(selected): Returns a list of variations for the selected Tigrinya characters.
    - selected_eng_rep(selected): Returns a list of English representations for the selected Tigrinya characters.
    - random_chars(): Generates a list of random Tigrinya characters for the quiz.
    - zip_chars(tig, eng): Zips Tigrinya characters with their corresponding English representations.
    - shuffle_characters(selected): Shuffles the order of selected Tigrinya characters for the quiz.
"""
import random

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

def selected_characters(selected):
    """
    Generates a list of variations for the selected Tigrinya characters.

    Args:
        selected (list): List of selected Tigrinya characters.
        
    Returns:
        list: List of variations for the selected Tigrinya characters.
    """
    idx_list = []
    sel_char_variation = []
    for c in selected:
        idx_list.append(TIGRINYA_CHARACTERS.index(c))
    for i in idx_list:
        sel_char_variation += CH_VARIATION[i]
    return sel_char_variation


def selected_eng_representations(selected):
    """
    Generates a list of English representations for the selected Tigrinya characters.
    
    Args:
        selected (list): List of selected Tigrinya characters.
        
    Returns:
        list: List of English representations for the selected Tigrinya characters.
    """
    idx_list = []
    eng_rep = []
    for c in selected:
        idx_list.append(TIGRINYA_CHARACTERS.index(c))
    for i in idx_list:
        eng_rep += CH_VARIATION_ENG_REP[i]
    return eng_rep


def random_chars():
    """
    Generates a list of random Tigrinya characters for the quiz.
    
    Returns:
        list: List of random Tigrinya characters.
    """
    random_idxs = random.sample(range(32), 5)
    rand_chars = []
    for idx in random_idxs:
        rand_chars.append(TIGRINYA_CHARACTERS[idx])
    return rand_chars


def zip_characters(tig, eng):
    """
    Zips Tigrinya characters with their corresponding English representations.
    
    Args:
        tig (list): List of Tigrinya characters.
        eng (list): List of English representations.
        
    Returns:
        zip: Zipped Tigrinya characters and English representations.
    """
    return zip(tig, eng)


def shuffle_characters(selected):
    """
    Shuffles the order of selected Tigrinya characters for the quiz.
    
    Args:
        selected (list): List of selected Tigrinya characters.
        
    Returns:
        list: Shuffled list of selected Tigrinya characters.
    """
    random.shuffle(selected)
    return selected
