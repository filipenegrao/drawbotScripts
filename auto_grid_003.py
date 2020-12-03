def auto_text_columns(txt, pg_size='A4Landscape', m_top=50, m_bottom=50, m_left=50, m_right=50, gutter=20, num_cols=2):
    
    t = txt
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
            if col == num_cols - 1:
                newPage(pg_size)
                left = x_origin
                continue
                
def add_header(txt, font_name_1="AvenirNext-Regular", font_name_2="AvenirNext-Bold", font_size=10, header_line=True, line_width=1, small_caps=True, m_top=50, m_bottom=50, m_left=50, m_right=50, pg_number=True):
        
    if header_line:
        stroke(0)
        strokeWidth(line_width)
        line((m_left, height()-m_top), (width()-m_right, height()-m_top))
    
    if small_caps:
        txt = txt.lower()
        openTypeFeatures(smcp=True)
                
    strokeWidth(0)
    font(font_name_1)
    text(txt, (m_left, height()-m_top+8))
    
    if pg_number:
        font(font_name_2)
        text(str(pageCount()), (width()-m_right, height()-m_top+8), align='right')
    
def add_footer(txt, font_name_1="AvenirNext-Regular", font_name_2="AvenirNext-Bold", font_size=10, header_line=True, line_width=1, small_caps=True, m_top=50, m_bottom=50, m_left=50, m_right=50, pg_number=True):
        
    if header_line:
        stroke(0)
        strokeWidth(line_width)
        line((m_left, m_bottom), (width()-m_right, m_bottom))
    
    if small_caps:
        txt = txt.lower()
        openTypeFeatures(smcp=True)
        
    strokeWidth(0)
    font(font_name_1)
    text(txt, (m_left, m_bottom-13)) 
    
    if pg_number:
        font(font_name_2)
        text(str(pageCount()), (width()-m_right, m_bottom-13), align='right')   

def oneline_fontinfo(font):
    fontSize(fontSize)

for p in range(10):
    newPage('A4Landscape')
    add_header('teste')
    add_footer('A fantástica fábrica de tipos')
