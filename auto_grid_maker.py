t = '''Lorem ipsum is a pseudo-Latin text used in web design, typography, layout, and printing in place of English to emphasise design elements over content. It's also called placeholder (or filler) text. It's a convenient tool for mock-ups. It helps to outline the visual elements of a document or presentation, eg typography, font, or layout. Lorem ipsum is mostly a part of a Latin text by the classical author and philosopher Cicero. Its words and letters have been changed by addition or removal, so to deliberately render its content nonsensical; it's not genuine, correct, or comprehensible Latin anymore. While lorem ipsum's still resembles classical Latin, it actually has no meaning whatsoever. As Cicero's text doesn't contain the letters K, W, or Z, alien to latin, these, and others are often inserted randomly to mimic the typographic appearence of European languages, as are digraphs not to be found in the original.
In a professional context it often happens that private or corporate clients corder a publication to be made and presented with the actual content still not being ready. Think of a news blog that's filled with content hourly on the day of going live. However, reviewers tend to be distracted by comprehensible content, say, a random text copied from a newspaper or the internet. The are likely to focus on the text, disregarding the layout and its elements. Besides, random text risks to be unintendedly humorous or offensive, an unacceptable risk in corporate environments. Lorem ipsum and its many variants have been employed since the early 1960ies, and quite likely since the sixteenth century.
Most of its text is made up from sections 1.10.32–3 of Cicero's De finibus bonorum et malorum (On the Boundaries of Goods and Evils; finibus may also be translated as purposes). Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit is the first known version ("Neither is there anyone who loves grief itself since it is grief and thus wants to obtain it"). It was found by Richard McClintock, a philologist, director of publications at Hampden-Sydney College in Virginia; he searched for citings of consectetur in classical Latin literature, a term of remarkably low frequency in that literary corpus.
Cicero famously orated against his political opponent Lucius Sergius Catilina. Occasionally the first Oration against Catiline is taken for type specimens: Quo usque tandem abutere, Catilina, patientia nostra? Quam diu etiam furor iste tuus nos eludet? (How long, O Catiline, will you abuse our patience? And for how long will that madness of yours mock us?)
'''

def col_grid(txt, page_size="A4Landscape", margin_top=50, margin_bottom=50, margin_left=50, margin_right=50,  num_cols=2, gutter=25, fontname="Verdana", fontsize=12): 
    
    # margins
    m_top = margin_top
    m_bottom = margin_bottom
    m_left = margin_left
    m_right = margin_right
    
    newPage(page_size)     
    # calculate pas/size 
    w = (width() - gutter * (num_cols + 1)) / num_cols - ((m_right + m_left) / num_cols)
    y = m_bottom
    font(fontname, fontsize)
    
    while len(txt):
        for col in range(num_cols):
            x = gutter + col * (w + gutter)
            h = height() - (m_top + m_bottom)
            txt = textBox(txt, (x, y, w, h))
        
col_grid(t, num_cols=3)