from systools import get_sel
from yat import auto_translate_ya


selected_text = get_sel()
yat_result = auto_translate_ya(selected_text)

import ipdb; ipdb.set_trace()
