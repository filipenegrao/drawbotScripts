t = '''Lorem ipsum is a pseudo-Latin text used in web design, typography, layout, and printing in place of English to emphasise design elements over content. It's also called placeholder (or filler) text. It's a convenient tool for mock-ups. It helps to outline the visual elements of a document or presentation, eg typography, font, or layout. Lorem ipsum is mostly a part of a Latin text by the classical author and philosopher Cicero. Its words and letters have been changed by addition or removal, so to deliberately render its content nonsensical; it's not genuine, correct, or comprehensible Latin anymore. While lorem ipsum's still resembles classical Latin, it actually has no meaning whatsoever. As Cicero's text doesn't contain the letters K, W, or Z, alien to latin, these, and others are often inserted randomly to mimic the typographic appearence of European languages, as are digraphs not to be found in the original.
In a professional context it often happens that private or corporate clients corder a publication to be made and presented with the actual content still not being ready. Think of a news blog that's filled with content hourly on the day of going live. However, reviewers tend to be distracted by comprehensible content, say, a random text copied from a newspaper or the internet. The are likely to focus on the text, disregarding the layout and its elements. Besides, random text risks to be unintendedly humorous or offensive, an unacceptable risk in corporate environments. Lorem ipsum and its many variants have been employed since the early 1960ies, and quite likely since the sixteenth century.
Most of its text is made up from sections 1.10.32–3 of Cicero's De finibus bonorum et malorum (On the Boundaries of Goods and Evils; finibus may also be translated as purposes). Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit is the first known version ("Neither is there anyone who loves grief itself since it is grief and thus wants to obtain it"). It was found by Richard McClintock, a philologist, director of publications at Hampden-Sydney College in Virginia; he searched for citings of consectetur in classical Latin literature, a term of remarkably low frequency in that literary corpus.
Cicero famously orated against his political opponent Lucius Sergius Catilina. Occasionally the first Oration against Catiline is taken for type specimens: Quo usque tandem abutere, Catilina, patientia nostra? Quam diu etiam furor iste tuus nos eludet? (How long, O Catiline, will you abuse our patience? And for how long will that madness of yours mock us?)
Andy made an equally compelling counterproposal, reminding me that the command-line editor — these days, home to so many people who design things — could really be improved by a fully fixed-width typeface. What if, in addition to shedding the unwanted baggage of the typewriter, we also looked to the programming environment as a place where type could make a difference? Like many screen fonts before it, Operator could pay extra attention to the brackets and braces and punctuation marks more critical in code than in text. But if Operator took the unusual step of looking not only to serifs and sans serifs, but to script typefaces for inspiration, it could do a lot more. It could render the easily-confused I, l, and 1 far less ambiguous. It could help “color” syntax in a way that transcends the actual use of color, ensuring that different parts of a program are easier to identify. Andy hoped this might be useful when a technical pdf found its way to a black-and-white laser printer. It was an especially meaningful gesture to me, as someone who, like three hundred million others, is red-green colorblind.
In developing Operator, we found ourselves talking about JavaScript and css, looking for vinyl label embossers on eBay, renting a cantankerous old machine from perhaps the last typewriter repair shop in New York, and unearthing a flea market find that amazingly dates to 1893. Above is the four-minute film I made, to record a little of what went into Operator, and introduce the team at H&Co behind it. —JH
Lorem ipsum is a pseudo-Latin text used in web design, typography, layout, and printing in place of English to emphasise design elements over content. It's also called placeholder (or filler) text. It's a convenient tool for mock-ups. It helps to outline the visual elements of a document or presentation, eg typography, font, or layout. Lorem ipsum is mostly a part of a Latin text by the classical author and philosopher Cicero. Its words and letters have been changed by addition or removal, so to deliberately render its content nonsensical; it's not genuine, correct, or comprehensible Latin anymore. While lorem ipsum's still resembles classical Latin, it actually has no meaning whatsoever. As Cicero's text doesn't contain the letters K, W, or Z, alien to latin, these, and others are often inserted randomly to mimic the typographic appearence of European languages, as are digraphs not to be found in the original.
In a professional context it often happens that private or corporate clients corder a publication to be made and presented with the actual content still not being ready. Think of a news blog that's filled with content hourly on the day of going live. However, reviewers tend to be distracted by comprehensible content, say, a random text copied from a newspaper or the internet. The are likely to focus on the text, disregarding the layout and its elements. Besides, random text risks to be unintendedly humorous or offensive, an unacceptable risk in corporate environments. Lorem ipsum and its many variants have been employed since the early 1960ies, and quite likely since the sixteenth century.
Most of its text is made up from sections 1.10.32–3 of Cicero's De finibus bonorum et malorum (On the Boundaries of Goods and Evils; finibus may also be translated as purposes). Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit is the first known version ("Neither is there anyone who loves grief itself since it is grief and thus wants to obtain it"). It was found by Richard McClintock, a philologist, director of publications at Hampden-Sydney College in Virginia; he searched for citings of consectetur in classical Latin literature, a term of remarkably low frequency in that literary corpus.
Cicero famously orated against his political opponent Lucius Sergius Catilina. Occasionally the first Oration against Catiline is taken for type specimens: Quo usque tandem abutere, Catilina, patientia nostra? Quam diu etiam furor iste tuus nos eludet? (How long, O Catiline, will you abuse our patience? And for how long will that madness of yours mock us?)
Andy made an equally compelling counterproposal, reminding me that the command-line editor — these days, home to so many people who design things — could really be improved by a fully fixed-width typeface. What if, in addition to shedding the unwanted baggage of the typewriter, we also looked to the programming environment as a place where type could make a difference? Like many screen fonts before it, Operator could pay extra attention to the brackets and braces and punctuation marks more critical in code than in text. But if Operator took the unusual step of looking not only to serifs and sans serifs, but to script typefaces for inspiration, it could do a lot more. It could render the easily-confused I, l, and 1 far less ambiguous. It could help “color” syntax in a way that transcends the actual use of color, ensuring that different parts of a program are easier to identify. Andy hoped this might be useful when a technical pdf found its way to a black-and-white laser printer. It was an especially meaningful gesture to me, as someone who, like three hundred million others, is red-green colorblind.
In developing Operator, we found ourselves talking about JavaScript and css, looking for vinyl label embossers on eBay, renting a cantankerous old machine from perhaps the last typewriter repair shop in New York, and unearthing a flea market find that amazingly dates to 1893. Above is the four-minute film I made, to record a little of what went into Operator, and introduce the team at H&Co behind it.'''

pg_size = 'A4Landscape'
pg = newPage(pg_size)

# margins
top, bottom, left, right = 100, 100, 100, 100
x_origin = left
gutter = 20
num_cols = 3

# mancha de texto
w = width() - left - right
h = height() - top - bottom
print(w, h)

col_w = (w / num_cols) - (gutter/2)

while len(t):
    for col in range(num_cols):
        t = textBox(t, (left, bottom, col_w, h))
        left = left + col_w + gutter
        if left >= w:
            newPage(pg_size)
            left = x_origin
            t = textBox(t, (left, bottom, col_w, h))
            left = left + col_w + gutter

def auto_text_columns(txt, pg_size='A4Landscape', m_top='50', m_bottom='50', m_left='50', m_right='50', gutter='20', num_cols='20'):
    
    pg = newPage(pg_size)

    # margins
    top, bottom, left, right =  m_top, m_bottom, m_left, m_right
    x_origin = left

    # mancha de texto
    w = width() - left - right
    h = height() - top - bottom
    print(w, h)

    col_w = (w / num_cols) - (gutter/2)

    while len(t):
        for col in range(num_cols):
            t = textBox(t, (left, bottom, col_w, h))
            left = left + col_w + gutter
            if left >= w:
                newPage(pg_size)
                left = x_origin
                t = textBox(t, (left, bottom, col_w, h))
                left = left + col_w + gutter