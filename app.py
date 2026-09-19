
import random
import html
import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# Myra's Study App
# Single-file Streamlit prototype
# Run with: streamlit run app.py
# =========================================================

st.set_page_config(
    page_title="Myra's Study App",
    page_icon="🌷",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# DATA
# -----------------------------

SCIENCE_UNITS = [
    {
        "id": 1,
        "tab": "บท 1\nตัวเรา",
        "title": "ตัวเรา พืช และสัตว์",
        "subtitle": "อวัยวะของเรา การดูแลร่างกาย และส่วนต่าง ๆ ของพืชและสัตว์",
        "reading": """
## หน่วยที่ 1 ตัวเรา พืช และสัตว์

ร่างกายของเราประกอบด้วยอวัยวะหลายส่วน แต่ละส่วนมีหน้าที่แตกต่างกัน และทำงานร่วมกันเพื่อให้เราดำเนินชีวิตได้ตามปกติ

**ตา** ใช้มองเห็นสิ่งต่าง ๆ เช่น สี รูปร่าง ขนาด และตำแหน่งของสิ่งของ เราควรอ่านหนังสือในที่ที่มีแสงเพียงพอ ไม่จ้องแสงที่สว่างมาก และไม่ใช้มือสกปรกขยี้ตา

**หู** ใช้ฟังเสียง ช่วยให้เรารับรู้เสียงดังและเสียงเบา รวมทั้งทิศทางของเสียง เราไม่ควรนำของแข็งหรือของแหลมเข้าไปในหู และควรหลีกเลี่ยงเสียงที่ดังเกินไป

**จมูก** ใช้หายใจและดมกลิ่น ส่วน **ลิ้น** ช่วยรับรสอาหารและช่วยในการพูด **ผิวหนัง** ช่วยรับความรู้สึก เช่น ร้อน เย็น นุ่ม แข็ง เรียบ หรือขรุขระ

**มือและแขน** ช่วยหยิบ จับ ถือ ผลัก และดึง ส่วน **ขาและเท้า** ช่วยยืน เดิน วิ่ง และกระโดด อวัยวะทุกส่วนมีความสำคัญ เราจึงควรรักษาความสะอาด รับประทานอาหารที่มีประโยชน์ พักผ่อนให้เพียงพอ และออกกำลังกายอย่างเหมาะสม

พืชก็เป็นสิ่งมีชีวิต พืชทั่วไปมีส่วนสำคัญ ได้แก่ **ราก ลำต้น ใบ ดอก ผล และเมล็ด**

**ราก** ช่วยยึดต้นพืชไว้กับดินและดูดน้ำกับแร่ธาตุ  
**ลำต้น** ช่วยพยุงส่วนต่าง ๆ ของพืชและลำเลียงน้ำ  
**ใบ** เป็นส่วนสำคัญที่ช่วยสร้างอาหารให้พืช  
**ดอก** เกี่ยวข้องกับการสืบพันธุ์  
**ผล** ช่วยห่อหุ้มเมล็ด  
**เมล็ด** สามารถเจริญเติบโตเป็นต้นพืชต้นใหม่เมื่อมีสภาพที่เหมาะสม

สัตว์ก็มีส่วนต่าง ๆ ของร่างกายที่ช่วยในการดำรงชีวิต เช่น นกมีปีกช่วยบิน ปลาใช้ครีบช่วยว่ายน้ำ และสัตว์บกหลายชนิดใช้ขาในการเดินหรือวิ่ง

### จำง่ายก่อนสอบ
- ตา = มองเห็น
- หู = ได้ยินเสียง
- จมูก = ดมกลิ่นและหายใจ
- ลิ้น = รับรส
- ราก = ยึดต้น + ดูดน้ำ
- ใบ = ช่วยสร้างอาหาร
- ปีก = ช่วยนกบิน
- ครีบ = ช่วยปลาว่ายน้ำ

สิ่งสำคัญของหน่วยนี้คือ **อวัยวะและส่วนต่าง ๆ ของสิ่งมีชีวิตมีหน้าที่แตกต่างกัน แต่ทำงานร่วมกันเพื่อให้สิ่งมีชีวิตดำรงชีวิตได้**
""",
        "practice": [
            {
                "id": "u1q1",
                "question": "อวัยวะใดใช้มองเห็น?",
                "choices": ["หู", "ตา", "จมูก"],
                "answer": "ตา",
                "explain": "ตาใช้มองเห็นสี รูปร่าง ขนาด และสิ่งต่าง ๆ รอบตัว"
            },
            {
                "id": "u1q2",
                "question": "ข้อใดเป็นวิธีดูแลหูที่เหมาะสม?",
                "choices": ["ใช้ของแหลมแคะหู", "ฟังเสียงดังมาก ๆ", "ไม่ใส่ของแหลมเข้าไปในหู"],
                "answer": "ไม่ใส่ของแหลมเข้าไปในหู",
                "explain": "การไม่ใส่ของแหลมเข้าไปในหูช่วยลดความเสี่ยงต่อการบาดเจ็บ"
            },
            {
                "id": "u1q3",
                "question": "ส่วนใดของพืชช่วยดูดน้ำจากดิน?",
                "choices": ["ราก", "ดอก", "ผล"],
                "answer": "ราก",
                "explain": "รากช่วยยึดต้นพืชกับดินและดูดน้ำกับแร่ธาตุ"
            },
            {
                "id": "u1q4",
                "question": "สัตว์ใดใช้ครีบช่วยในการเคลื่อนที่?",
                "choices": ["ปลา", "แมว", "นก"],
                "answer": "ปลา",
                "explain": "ปลาใช้ครีบช่วยว่ายน้ำและควบคุมการเคลื่อนที่"
            },
            {
                "id": "u1q5",
                "question": "ส่วนใดของพืชช่วยห่อหุ้มเมล็ด?",
                "choices": ["ผล", "ราก", "ใบ"],
                "answer": "ผล",
                "explain": "ผลช่วยห่อหุ้มหรือปกป้องเมล็ด"
            },
        ],
    },
    {
        "id": 2,
        "tab": "บท 2\nพืชและสัตว์",
        "title": "พืชและสัตว์ในท้องถิ่น",
        "subtitle": "สำรวจสิ่งมีชีวิตรอบตัวและสถานที่ที่เหมาะกับการดำรงชีวิต",
        "reading": """
## หน่วยที่ 2 พืชและสัตว์ในท้องถิ่น

รอบตัวเรามีพืชและสัตว์อาศัยอยู่ในบริเวณที่แตกต่างกัน เช่น บ้าน โรงเรียน สวน ทุ่งนา ป่า บ่อน้ำ ลำคลอง หรือแหล่งน้ำต่าง ๆ

บริเวณหนึ่งอาจพบสิ่งมีชีวิตหลายชนิด เช่น ในสวนอาจพบต้นไม้ หญ้า ดอกไม้ มด ผีเสื้อ นก และไส้เดือน ส่วนบริเวณบ่อน้ำอาจพบปลา กบ แมลงน้ำ และพืชน้ำ

สิ่งมีชีวิตแต่ละชนิดต้องการสภาพแวดล้อมที่เหมาะสม เช่น **น้ำ อาหาร แสงแดด อากาศ ดิน และที่หลบภัย** จึงทำให้เราไม่ได้พบพืชและสัตว์ชนิดเดียวกันในทุกสถานที่

การเรียนวิทยาศาสตร์ในหน่วยนี้เน้นการ **สังเกต สำรวจ บันทึก และเปรียบเทียบ** เช่น เราอาจเดินสำรวจบริเวณโรงเรียน แล้วบันทึกว่าพบพืชชนิดใด พบสัตว์ชนิดใด และสิ่งมีชีวิตเหล่านั้นอยู่บริเวณไหน

เมื่อสำรวจธรรมชาติ เราควรปฏิบัติอย่างระมัดระวัง ไม่เด็ดต้นไม้โดยไม่จำเป็น ไม่ทำลายรังสัตว์ และไม่ทำร้ายสิ่งมีชีวิต เพราะพืชและสัตว์เป็นส่วนหนึ่งของธรรมชาติและสิ่งแวดล้อม

### ตัวอย่างการสังเกต
- สวน: ต้นไม้ หญ้า ผีเสื้อ มด นก
- บ่อน้ำ: ปลา กบ พืชน้ำ
- ใต้ก้อนหินหรือดินชื้น: อาจพบมด ไส้เดือน หรือแมลงบางชนิด

### จำง่ายก่อนสอบ
**สถานที่ต่างกัน → สิ่งมีชีวิตที่พบอาจต่างกัน**  
เพราะสิ่งมีชีวิตแต่ละชนิดต้องการสภาพแวดล้อมที่เหมาะสมกับการดำรงชีวิต

สิ่งสำคัญของหน่วยนี้คือ การใช้ตาและประสาทสัมผัสอย่างปลอดภัยเพื่อสังเกตสิ่งรอบตัว แล้วอธิบายจากสิ่งที่เห็นจริง
""",
        "practice": [
            {
                "id": "u2q1",
                "question": "บริเวณใดมีโอกาสพบปลาได้มากที่สุด?",
                "choices": ["บ่อน้ำ", "สนามแห้ง", "โต๊ะเรียน"],
                "answer": "บ่อน้ำ",
                "explain": "ปลาอาศัยอยู่ในน้ำ จึงพบได้ในบ่อน้ำหรือแหล่งน้ำ"
            },
            {
                "id": "u2q2",
                "question": "ข้อใดเป็นการสำรวจธรรมชาติอย่างเหมาะสม?",
                "choices": ["ทำลายรังสัตว์", "สังเกตและบันทึก", "เด็ดต้นไม้ทุกต้น"],
                "answer": "สังเกตและบันทึก",
                "explain": "การสังเกตและบันทึกช่วยให้เรียนรู้โดยไม่ทำร้ายสิ่งมีชีวิต"
            },
            {
                "id": "u2q3",
                "question": "สิ่งมีชีวิตต้องการสิ่งใดเพื่อดำรงชีวิต?",
                "choices": ["น้ำและอาหาร", "ของเล่น", "โทรศัพท์"],
                "answer": "น้ำและอาหาร",
                "explain": "สิ่งมีชีวิตต้องการน้ำ อาหาร อากาศ และสภาพแวดล้อมที่เหมาะสม"
            },
            {
                "id": "u2q4",
                "question": "ทำไมจึงพบพืชและสัตว์ไม่เหมือนกันในทุกสถานที่?",
                "choices": ["เพราะสภาพแวดล้อมต่างกัน", "เพราะชื่อสถานที่ต่างกัน", "เพราะสีพื้นต่างกัน"],
                "answer": "เพราะสภาพแวดล้อมต่างกัน",
                "explain": "สิ่งมีชีวิตแต่ละชนิดเหมาะกับสภาพแวดล้อมต่างกัน"
            },
            {
                "id": "u2q5",
                "question": "สิ่งใดอาจพบในสวน?",
                "choices": ["ผีเสื้อ", "ปลาวาฬ", "ฉลาม"],
                "answer": "ผีเสื้อ",
                "explain": "ผีเสื้อมักพบตามสวนหรือบริเวณที่มีดอกไม้"
            },
        ],
    },
    {
        "id": 3,
        "tab": "บท 3\nวัสดุรอบตัวเรา",
        "title": "วัสดุรอบตัวเรา",
        "subtitle": "รู้จักวัตถุ วัสดุ และสมบัติของวัสดุที่ใช้ในชีวิตประจำวัน",
        "reading": """
## หน่วยที่ 3 วัสดุรอบตัวเรา

ในชีวิตประจำวัน เราพบสิ่งของหรือ **วัตถุ** มากมาย เช่น โต๊ะ เก้าอี้ ขวดน้ำ ดินสอ แก้วน้ำ เสื้อผ้า และของเล่น สิ่งของเหล่านี้ทำมาจาก **วัสดุ** หลายชนิด

**วัตถุ** คือสิ่งของที่เรามองเห็นหรือจับต้องได้ ส่วน **วัสดุ** คือสิ่งที่นำมาใช้ทำวัตถุ เช่น โต๊ะเป็นวัตถุ ส่วนไม้เป็นวัสดุ ขวดน้ำเป็นวัตถุ ส่วนพลาสติกเป็นวัสดุ

วัสดุที่พบได้บ่อย ได้แก่ **ไม้ พลาสติก แก้ว โลหะ ผ้า กระดาษ และยาง** วัสดุแต่ละชนิดมีสมบัติไม่เหมือนกัน จึงเหมาะกับการใช้งานต่างกัน

### ไม้
ไม้ส่วนใหญ่มักมีความแข็งและแข็งแรง จึงนำไปทำโต๊ะ เก้าอี้ ประตู หรือของเล่นบางชนิดได้

### พลาสติก
พลาสติกมีหลายชนิด บางชนิดอ่อน บางชนิดแข็ง มีน้ำหนักค่อนข้างเบา และขึ้นรูปได้หลากหลาย จึงใช้ทำขวด กล่อง ของเล่น และของใช้ต่าง ๆ

### แก้ว
แก้วหลายชนิดมีความใส จึงมองผ่านได้ แต่แตกได้ง่าย จึงต้องใช้อย่างระมัดระวัง

### โลหะ
โลหะหลายชนิดมีความแข็งแรงและทนทาน บางชนิดนำความร้อนได้ จึงใช้ทำช้อน หม้อ เครื่องมือ หรือชิ้นส่วนต่าง ๆ

### ผ้า
ผ้ามักอ่อนนุ่ม พับได้ และเหมาะสำหรับทำเสื้อผ้า ผ้าห่ม หรือผ้าเช็ดตัว

### ยาง
ยางหลายชนิดมีความยืดหยุ่น เช่น หนังยาง หรือยางที่ใช้ทำสิ่งของบางประเภท

สิ่งของหนึ่งชิ้นอาจทำจากวัสดุเพียงชนิดเดียว หรือทำจากวัสดุหลายชนิดก็ได้ เช่น ดินสอหนึ่งแท่งอาจประกอบด้วยไม้ ไส้ดินสอ โลหะ และยางลบ

เราจึงเลือกวัสดุให้เหมาะกับการใช้งาน โดยพิจารณาจากสมบัติของวัสดุ เช่น หากต้องการสิ่งของที่มองผ่านได้ อาจเลือกวัสดุใส หากต้องการสิ่งของที่แข็งแรง อาจเลือกไม้หรือโลหะ

### จำง่ายก่อนสอบ
- วัตถุ = สิ่งของ
- วัสดุ = สิ่งที่ใช้ทำสิ่งของ
- แก้ว = มักใส มองผ่านได้ แต่แตกง่าย
- ผ้า = นุ่ม พับได้
- โลหะ = มักแข็งแรง
- ยาง = หลายชนิดยืดหยุ่น
- เลือกวัสดุให้เหมาะกับงาน

สิ่งสำคัญของหน่วยนี้คือ **วัสดุแต่ละชนิดมีสมบัติต่างกัน จึงนำไปใช้ประโยชน์ต่างกัน**
""",
        "practice": [
            {
                "id": "u3q1",
                "question": "โต๊ะคืออะไร?",
                "choices": ["วัตถุ", "วัสดุ", "แสง"],
                "answer": "วัตถุ",
                "explain": "โต๊ะเป็นสิ่งของ จึงเป็นวัตถุ"
            },
            {
                "id": "u3q2",
                "question": "ไม้ที่ใช้ทำโต๊ะคืออะไร?",
                "choices": ["วัตถุ", "วัสดุ", "เสียง"],
                "answer": "วัสดุ",
                "explain": "ไม้เป็นวัสดุที่นำมาใช้ทำสิ่งของ เช่น โต๊ะหรือเก้าอี้"
            },
            {
                "id": "u3q3",
                "question": "วัสดุใดมองผ่านได้?",
                "choices": ["ไม้", "แก้ว", "ผ้า"],
                "answer": "แก้ว",
                "explain": "แก้วหลายชนิดมีความใส จึงมองผ่านได้"
            },
            {
                "id": "u3q4",
                "question": "วัสดุใดมักอ่อนนุ่มและพับได้?",
                "choices": ["ผ้า", "หิน", "โลหะ"],
                "answer": "ผ้า",
                "explain": "ผ้ามักอ่อนนุ่มและพับได้"
            },
            {
                "id": "u3q5",
                "question": "สิ่งของหนึ่งชิ้นทำจากวัสดุหลายชนิดได้หรือไม่?",
                "choices": ["ได้", "ไม่ได้", "ได้เฉพาะของเล่น"],
                "answer": "ได้",
                "explain": "เช่น ดินสออาจมีไม้ ไส้ดินสอ โลหะ และยางลบ"
            },
        ],
    },
    {
        "id": 4,
        "tab": "บท 4\nหินและท้องฟ้า",
        "title": "หินและท้องฟ้าของเรา",
        "subtitle": "สังเกตลักษณะของหิน และสิ่งที่เห็นบนท้องฟ้ากลางวันและกลางคืน",
        "reading": """
## หน่วยที่ 4 หินและท้องฟ้าของเรา

หินเป็นสิ่งที่พบได้ตามธรรมชาติ เราสามารถพบหินได้ตามพื้นดิน ภูเขา ลำธาร ชายหาด หรือบริเวณต่าง ๆ

หินแต่ละก้อนอาจมีลักษณะไม่เหมือนกัน เราสามารถสังเกตได้จาก **สี รูปร่าง ขนาด ลวดลาย ผิวสัมผัส และความแข็ง**

หินบางก้อนมีผิวเรียบ บางก้อนมีผิวขรุขระ บางก้อนมีสีเดียว ขณะที่บางก้อนมีลวดลายหลายสี เราสามารถนำหินมาเปรียบเทียบและจัดกลุ่มตามลักษณะที่เหมือนกัน เช่น แบ่งตามสี ขนาด หรือผิวสัมผัส

การสังเกตทางวิทยาศาสตร์ควรใช้สิ่งที่เราสามารถเห็น สัมผัส หรือเปรียบเทียบได้ และควรบอกตามสิ่งที่สังเกตจริง

### ท้องฟ้าเวลากลางวัน
ในเวลากลางวัน เรามักเห็นดวงอาทิตย์และท้องฟ้าสว่าง ดวงอาทิตย์เป็นแหล่งแสงสำคัญและให้ความร้อนแก่โลก

เรา **ไม่ควรจ้องดวงอาทิตย์ด้วยตาเปล่า** เพราะแสงที่แรงสามารถทำอันตรายต่อดวงตาได้

### ท้องฟ้าเวลากลางคืน
เมื่อถึงเวลากลางคืน ท้องฟ้าจะมืดลง เราอาจมองเห็นดวงจันทร์และดาว

ดวงจันทร์ที่มองเห็นในแต่ละคืนอาจมีส่วนสว่างแตกต่างกัน บางคืนเห็นมาก บางคืนเห็นน้อย ส่วนดาวบนท้องฟ้ามองเห็นเป็นจุดสว่าง แต่บางคืนอาจมองเห็นดาวไม่ชัดเพราะเมฆหรือแสงจากบริเวณรอบ ๆ

### จำง่ายก่อนสอบ
- หินแต่ละก้อนมีลักษณะต่างกัน
- ใช้สี รูปร่าง ขนาด และผิวสัมผัสช่วยเปรียบเทียบหิน
- กลางวันมักเห็นดวงอาทิตย์
- กลางคืนมักเห็นดวงจันทร์และดาว
- ไม่จ้องดวงอาทิตย์โดยตรง

สิ่งสำคัญของหน่วยนี้คือ **ฝึกสังเกต เปรียบเทียบ และอธิบายสิ่งที่เห็นจากธรรมชาติ**
""",
        "practice": [
            {
                "id": "u4q1",
                "question": "ข้อใดใช้เปรียบเทียบหินได้?",
                "choices": ["สีและผิวสัมผัส", "ชื่อเจ้าของ", "ราคาของเล่น"],
                "answer": "สีและผิวสัมผัส",
                "explain": "เราสามารถเปรียบเทียบหินจากสี รูปร่าง ขนาด และผิวสัมผัส"
            },
            {
                "id": "u4q2",
                "question": "เวลากลางวันมักเห็นสิ่งใดบนท้องฟ้า?",
                "choices": ["ดวงอาทิตย์", "โคมไฟ", "โทรศัพท์"],
                "answer": "ดวงอาทิตย์",
                "explain": "กลางวันเรามักเห็นดวงอาทิตย์และท้องฟ้าสว่าง"
            },
            {
                "id": "u4q3",
                "question": "เวลากลางคืนอาจเห็นอะไรบนท้องฟ้า?",
                "choices": ["ดวงจันทร์และดาว", "โต๊ะและเก้าอี้", "ดินสอและยางลบ"],
                "answer": "ดวงจันทร์และดาว",
                "explain": "กลางคืนเรามักสังเกตเห็นดวงจันทร์และดาว"
            },
            {
                "id": "u4q4",
                "question": "เราควรจ้องดวงอาทิตย์ด้วยตาเปล่าหรือไม่?",
                "choices": ["ไม่ควร", "ควร", "ควรเฉพาะตอนเที่ยง"],
                "answer": "ไม่ควร",
                "explain": "แสงจากดวงอาทิตย์ที่แรงสามารถทำอันตรายต่อดวงตาได้"
            },
            {
                "id": "u4q5",
                "question": "หินทุกก้อนมีลักษณะเหมือนกันหรือไม่?",
                "choices": ["ไม่เหมือนกันทุกก้อน", "เหมือนกันทั้งหมด", "มีสีเดียวทั้งหมด"],
                "answer": "ไม่เหมือนกันทุกก้อน",
                "explain": "หินอาจมีสี รูปร่าง ขนาด และพื้นผิวต่างกัน"
            },
        ],
    },
]

SUBJECTS = [
    ("🔬", "Science", "วิทยาศาสตร์", "science", "#E8FFF6"),
    ("🧮", "Maths", "คณิตศาสตร์", "maths", "#FFF7DE"),
    ("🔤", "English", "ภาษาอังกฤษ", "english", "#FFEAF1"),
    ("📖", "ภาษาไทย", "ภาษาไทย", "thai", "#FFF2E2"),
    ("🏮", "Chinese", "ภาษาจีน", "chinese", "#FFF0F0"),
    ("🌍", "Social", "สังคมศึกษา", "social", "#EAF4FF"),
    ("🔡", "Phonics", "การออกเสียง", "phonics", "#F4EEFF"),
    ("💻", "Coding", "การเขียนโปรแกรม", "coding", "#EAF9FF"),
]

# -----------------------------
# STATE
# -----------------------------

defaults = {
    "page": "home",
    "subject": None,
    "unit_id": 1,
    "section": "reading",
    "wrong_ids": set(),
    "answered": {},
    "test_questions": [],
    "test_index": 0,
    "test_answers": {},
    "test_finished": False,
    "test_mode": None,
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -----------------------------
# HELPERS
# -----------------------------

def get_unit(unit_id):
    return next(u for u in SCIENCE_UNITS if u["id"] == unit_id)

def all_science_questions():
    questions = []
    for unit in SCIENCE_UNITS:
        for q in unit["practice"]:
            item = dict(q)
            item["unit_id"] = unit["id"]
            item["unit_title"] = unit["title"]
            questions.append(item)
    return questions

def question_by_id(qid):
    for q in all_science_questions():
        if q["id"] == qid:
            return q
    return None

def go_home():
    st.session_state.page = "home"
    st.session_state.subject = None
    st.session_state.section = "reading"
    st.rerun()

def go_science():
    st.session_state.page = "subject"
    st.session_state.subject = "science"
    st.rerun()

def read_aloud_button(text, key):
    """
    แถบฟังอ่านสำหรับบทเรียนยาว:
    ↶ ย้อนประมาณ 10%
    ▶/⏸ เล่น / หยุดชั่วคราว / เล่นต่อ
    ↷ ไปข้างหน้าประมาณ 10%
    ลากแถบเพื่อข้ามไปยังตำแหน่งที่ต้องการ
    """
    safe_text = html.escape(text).replace("\n", " ")
    safe_js = (
        safe_text
        .replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace("${", "\\${")
    )

    components.html(
        f"""
        <div class="readbar-wrap">
          <div class="readbar-controls">
            <button class="round-btn" id="back_{key}" title="ย้อนกลับ">↶</button>
            <button class="round-btn play-btn" id="play_{key}" title="เล่น / หยุดชั่วคราว">▶</button>
            <button class="round-btn" id="forward_{key}" title="ไปข้างหน้า">↷</button>

            <input id="progress_{key}" class="read-slider"
                   type="range" min="0" max="100" value="0" step="1"
                   aria-label="ตำแหน่งการอ่าน">

            <div class="read-percent" id="percent_{key}">0%</div>
          </div>

          <div class="readbar-caption">
            🔊 ฟังอ่าน · กด ▶ เพื่อเริ่ม · กด ⏸ เพื่อหยุดชั่วคราว · ลากแถบเพื่อเลื่อนไปในบท
          </div>
        </div>

        <style>
          .readbar-wrap {{
            box-sizing: border-box;
            width: 100%;
            border-radius: 24px;
            padding: 14px 16px 10px 16px;
            margin: 4px 0 8px 0;
            background: linear-gradient(
              100deg,
              rgba(255,220,232,.92) 0%,
              rgba(255,237,205,.92) 22%,
              rgba(223,243,211,.92) 45%,
              rgba(211,239,245,.92) 68%,
              rgba(227,218,249,.92) 100%
            );
            border: 1px solid rgba(183,169,205,.30);
            box-shadow: 0 7px 18px rgba(92,102,130,.08);
            font-family: "Noto Sans Thai", Tahoma, sans-serif;
          }}

          .readbar-controls {{
            display: grid;
            grid-template-columns: 46px 46px 46px minmax(120px, 1fr) 48px;
            gap: 9px;
            align-items: center;
          }}

          .round-btn {{
            width: 44px;
            height: 44px;
            border: 1px solid rgba(125,111,145,.22);
            border-radius: 50%;
            background: rgba(255,255,255,.84);
            color: #66566f;
            font-size: 20px;
            font-weight: 800;
            cursor: pointer;
            box-shadow: 0 3px 8px rgba(90,86,110,.07);
          }}

          .round-btn:hover {{
            transform: translateY(-1px);
          }}

          .play-btn {{
            background: linear-gradient(
              135deg,
              #ffd8e7 0%,
              #ffe8c7 28%,
              #dff2d2 53%,
              #d7edf9 76%,
              #e6dcf8 100%
            );
          }}

          .read-slider {{
            width: 100%;
            accent-color: #b99bd7;
            cursor: pointer;
          }}

          .read-percent {{
            text-align: right;
            font-size: 17px;
            font-weight: 800;
            color: #705d76;
            white-space: nowrap;
          }}

          .readbar-caption {{
            margin-top: 7px;
            color: #7b687c;
            font-size: 13px;
            line-height: 1.35;
          }}

          @media (max-width: 520px) {{
            .readbar-wrap {{
              padding: 12px 11px 9px 11px;
              border-radius: 20px;
            }}
            .readbar-controls {{
              grid-template-columns: 40px 40px 40px minmax(80px, 1fr) 42px;
              gap: 6px;
            }}
            .round-btn {{
              width: 39px;
              height: 39px;
              font-size: 18px;
            }}
            .read-percent {{
              font-size: 15px;
            }}
            .readbar-caption {{
              font-size: 12px;
            }}
          }}
        </style>

        <script>
          (() => {{
            const fullText = `{safe_js}`;
            const synth = window.speechSynthesis;

            const playBtn = document.getElementById("play_{key}");
            const backBtn = document.getElementById("back_{key}");
            const forwardBtn = document.getElementById("forward_{key}");
            const slider = document.getElementById("progress_{key}");
            const percent = document.getElementById("percent_{key}");

            let utterance = null;
            let startIndex = 0;
            let absoluteIndex = 0;
            let isPlaying = false;
            let isPaused = false;

            function clamp(n, lo, hi) {{
              return Math.max(lo, Math.min(hi, n));
            }}

            function indexFromPercent(p) {{
              return Math.floor((clamp(p, 0, 100) / 100) * fullText.length);
            }}

            function percentFromIndex(i) {{
              if (!fullText.length) return 0;
              return clamp(Math.round((i / fullText.length) * 100), 0, 100);
            }}

            function setProgressFromIndex(i) {{
              absoluteIndex = clamp(i, 0, fullText.length);
              const p = percentFromIndex(absoluteIndex);
              slider.value = p;
              percent.textContent = p + "%";
            }}

            function chooseThaiVoice(u) {{
              const voices = synth.getVoices();
              const thaiVoice = voices.find(v =>
                (v.lang || "").toLowerCase().startsWith("th")
              );
              if (thaiVoice) u.voice = thaiVoice;
            }}

            function stopSpeech() {{
              synth.cancel();
              utterance = null;
              isPlaying = false;
              isPaused = false;
              playBtn.textContent = "▶";
            }}

            function speakFrom(index) {{
              stopSpeech();

              startIndex = clamp(index, 0, fullText.length);
              absoluteIndex = startIndex;

              if (startIndex >= fullText.length) {{
                setProgressFromIndex(fullText.length);
                return;
              }}

              const remaining = fullText.slice(startIndex);
              utterance = new SpeechSynthesisUtterance(remaining);
              utterance.lang = "th-TH";
              utterance.rate = 0.92;
              utterance.pitch = 1.03;
              chooseThaiVoice(utterance);

              utterance.onstart = () => {{
                isPlaying = true;
                isPaused = false;
                playBtn.textContent = "⏸";
              }};

              utterance.onboundary = (event) => {{
                if (typeof event.charIndex === "number") {{
                  setProgressFromIndex(startIndex + event.charIndex);
                }}
              }};

              utterance.onend = () => {{
                setProgressFromIndex(fullText.length);
                isPlaying = false;
                isPaused = false;
                playBtn.textContent = "▶";
              }};

              utterance.onerror = () => {{
                isPlaying = false;
                isPaused = false;
                playBtn.textContent = "▶";
              }};

              synth.speak(utterance);
            }}

            playBtn.addEventListener("click", () => {{
              if (isPlaying && !isPaused) {{
                synth.pause();
                isPaused = true;
                playBtn.textContent = "▶";
                return;
              }}

              if (isPlaying && isPaused) {{
                synth.resume();
                isPaused = false;
                playBtn.textContent = "⏸";
                return;
              }}

              speakFrom(indexFromPercent(Number(slider.value)));
            }});

            backBtn.addEventListener("click", () => {{
              const idx = indexFromPercent(Number(slider.value));
              const jump = Math.max(1, Math.floor(fullText.length * 0.10));
              const nextIndex = clamp(idx - jump, 0, fullText.length);
              setProgressFromIndex(nextIndex);
              speakFrom(nextIndex);
            }});

            forwardBtn.addEventListener("click", () => {{
              const idx = indexFromPercent(Number(slider.value));
              const jump = Math.max(1, Math.floor(fullText.length * 0.10));
              const nextIndex = clamp(idx + jump, 0, fullText.length);
              setProgressFromIndex(nextIndex);
              speakFrom(nextIndex);
            }});

            slider.addEventListener("input", () => {{
              percent.textContent = Math.round(Number(slider.value)) + "%";
            }});

            slider.addEventListener("change", () => {{
              const idx = indexFromPercent(Number(slider.value));
              setProgressFromIndex(idx);
              if (isPlaying || isPaused) {{
                speakFrom(idx);
              }}
            }});

            window.addEventListener("beforeunload", () => synth.cancel());
          }})();
        </script>
        """,
        height=112,
        scrolling=False,
    )


def start_test(mode, unit_id=None):
    pool = all_science_questions()

    if mode == "unit" and unit_id is not None:
        pool = [q for q in pool if q["unit_id"] == unit_id]
        size = len(pool)
    elif mode == "wrong":
        pool = [q for q in pool if q["id"] in st.session_state.wrong_ids]
        size = len(pool)
    elif mode == "book":
        size = min(12, len(pool))
    else:
        size = min(15, len(pool))

    if not pool:
        st.session_state.test_questions = []
        st.session_state.test_mode = mode
        st.session_state.test_finished = True
        return

    shuffled = pool[:]
    random.shuffle(shuffled)
    st.session_state.test_questions = shuffled[:size]
    st.session_state.test_index = 0
    st.session_state.test_answers = {}
    st.session_state.test_finished = False
    st.session_state.test_mode = mode

def save_test_answer(q, answer):
    st.session_state.test_answers[q["id"]] = answer
    if answer != q["answer"]:
        st.session_state.wrong_ids.add(q["id"])
    else:
        # ถ้าทำซ้ำในโหมดข้อที่เคยผิดแล้วตอบถูก ให้ลบออกจากรายการ
        if st.session_state.test_mode == "wrong":
            st.session_state.wrong_ids.discard(q["id"])

# -----------------------------
# STYLING
# -----------------------------

st.markdown(
    """
<style>
:root {
  --pink:#ff7aa8;
  --mint:#9fe6c2;
  --sky:#a9d9ff;
  --cream:#fffaf3;
  --lav:#d7c5ff;
  --ink:#26415e;
}

html, body, [class*="css"] {
  font-family: "Noto Sans Thai", "Tahoma", sans-serif;
}

.stApp {
  background:
    radial-gradient(circle at 10% 8%, rgba(255, 220, 232, .75), transparent 25%),
    radial-gradient(circle at 90% 14%, rgba(203, 232, 255, .75), transparent 24%),
    linear-gradient(180deg, #fffaf7 0%, #fbfdff 100%);
  color: var(--ink);
}

.block-container {
  max-width: 930px;
  padding-top: 1.3rem;
  padding-bottom: 5rem;
}

h1, h2, h3 {
  color:#284b70;
}

.app-hero {
  background:rgba(255,255,255,.86);
  border:1px solid rgba(255,255,255,.9);
  box-shadow:0 10px 30px rgba(90,120,150,.08);
  border-radius:28px;
  padding:22px 22px 18px 22px;
  text-align:center;
  margin-bottom:16px;
}

.app-title {
  font-size:2.45rem;
  line-height:1.05;
  font-weight:900;
  letter-spacing:-.04em;
  margin:0;
}

.app-title .p1 {color:#ff6f9e;}
.app-title .p2 {color:#5b9fe8;}
.app-title .p3 {color:#55bd8b;}

.subtle {
  color:#71869b;
  font-size:.95rem;
}

.subject-card {
  border-radius:24px;
  padding:18px 14px;
  min-height:138px;
  background:white;
  box-shadow:0 8px 22px rgba(75, 108, 145, .08);
  border:1px solid #edf1f5;
  text-align:center;
  margin-bottom:8px;
}

.subject-icon {
  font-size:2.35rem;
  line-height:1;
  margin-bottom:10px;
}

.subject-en {
  font-size:1.05rem;
  font-weight:800;
  color:#294b70;
}

.subject-th {
  font-size:.82rem;
  color:#7a8ea2;
}

.big-panel {
  background:rgba(255,255,255,.9);
  border-radius:24px;
  padding:18px;
  box-shadow:0 8px 22px rgba(75, 108, 145, .07);
  border:1px solid #edf1f5;
}

.reading-card {
  background:rgba(255,255,255,.96);
  border-radius:26px;
  padding:22px 22px 26px 22px;
  box-shadow:0 8px 26px rgba(75, 108, 145, .08);
  border:1px solid #edf1f5;
  font-size:1.04rem;
  line-height:1.86;
}

/* =========================================================
   PINNED CHAPTER NAV + AUDIO BAR
   Use position:fixed instead of sticky so it reliably stays
   visible in Streamlit while the long lesson scrolls.
   ========================================================= */
.st-key-chapter_nav {
  position: fixed !important;
  top: 4.15rem !important;
  left: 50% !important;
  transform: translateX(-50%) !important;

  width: min(900px, calc(100vw - 2.2rem)) !important;
  max-width: 900px !important;

  z-index: 999999 !important;

  background: rgba(255, 252, 249, .97) !important;
  border: 1px solid rgba(231, 226, 236, .96) !important;
  border-radius: 24px !important;

  padding: 9px 10px 7px 10px !important;
  margin: 0 !important;

  box-shadow: 0 10px 30px rgba(67, 80, 110, .14) !important;

  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);

  box-sizing: border-box !important;
}

/* Keep the 4 chapter buttons in one row */
.st-key-chapter_nav div[data-testid="stHorizontalBlock"] {
  gap: .48rem !important;
  flex-wrap: nowrap !important;
}

.st-key-chapter_nav div[data-testid="column"] {
  min-width: 0 !important;
  flex: 1 1 0 !important;
}

.st-key-chapter_nav div[data-testid="stButton"] > button {
  width: 100% !important;
  min-height: 56px !important;
  line-height: 1.2 !important;
  padding: .35rem .35rem !important;
  white-space: normal !important;
}

/* Audio component sits directly below chapter buttons */
.st-key-chapter_nav iframe {
  display: block !important;
  width: 100% !important;
  margin: 4px 0 0 0 !important;
  border: 0 !important;
  border-radius: 20px !important;
}

/* Spacer so normal content starts below the fixed toolbar */
.chapter-fixed-spacer {
  height: 190px;
}

/* Slightly smaller on phone */
@media (max-width: 650px) {
  .st-key-chapter_nav {
    top: 3.75rem !important;
    width: calc(100vw - 1rem) !important;
    border-radius: 20px !important;
    padding: 7px 7px 5px 7px !important;
  }

  .st-key-chapter_nav div[data-testid="stHorizontalBlock"] {
    gap: .28rem !important;
  }

  .st-key-chapter_nav div[data-testid="stButton"] > button {
    min-height: 52px !important;
    font-size: .78rem !important;
    padding: .22rem .16rem !important;
  }

  .chapter-fixed-spacer {
    height: 184px;
  }
}

.section-strip {
  background:rgba(255,255,255,.88);
  border:1px solid #eef1f4;
  padding:8px;
  border-radius:20px;
  margin-bottom:10px;
}

.quiz-box {
  border-radius:24px;
  padding:18px 18px 12px 18px;
  background:white;
  border:1px solid #edf1f5;
  box-shadow:0 8px 24px rgba(75,108,145,.07);
  margin-bottom:14px;
}

.good {
  background:#e8fbef;
  border:1px solid #a9e2bc;
  border-radius:18px;
  padding:14px 16px;
  color:#23613b;
  margin-top:10px;
}

.bad {
  background:#fff0f3;
  border:1px solid #ffc2d1;
  border-radius:18px;
  padding:14px 16px;
  color:#8b3550;
  margin-top:10px;
}

.mistake-card {
  border-radius:18px;
  background:white;
  border:1px solid #eef1f5;
  padding:14px 16px;
  margin-bottom:10px;
}

div[data-testid="stButton"] > button {
  border-radius:18px;
  min-height:46px;
  font-weight:700;
  border:1px solid #e7ebef;
}

div[data-testid="stButton"] > button:hover {
  border-color:#9ac8ff;
  color:#274f79;
}

/* Pastel-rainbow selected navigation instead of Streamlit bright red */
div[data-testid="stButton"] > button[kind="primary"],
button[kind="primary"] {
  background: linear-gradient(
    110deg,
    #f7cedd 0%,
    #f9dfbd 23%,
    #dcebcf 47%,
    #cfe5f5 72%,
    #ded4f3 100%
  ) !important;
  color: #51495e !important;
  border: 1px solid rgba(137,122,155,.20) !important;
  box-shadow: 0 5px 14px rgba(113,105,137,.08) !important;
}

div[data-testid="stButton"] > button[kind="primary"]:hover,
button[kind="primary"]:hover {
  filter: brightness(1.015);
  color: #443d50 !important;
  border-color: rgba(122,109,143,.28) !important;
}

div[data-testid="column"] {
  min-width:0;
}

@media (max-width: 650px) {
  .block-container {
    padding-left: .8rem;
    padding-right: .8rem;
    padding-top: .7rem;
  }
  .app-title { font-size:1.95rem; }
  .subject-card { min-height:120px; padding:14px 8px; }
  .subject-icon { font-size:1.9rem; }
  .subject-en { font-size:.92rem; }
  .subject-th { font-size:.75rem; }
  .reading-card { padding:18px 16px 22px 16px; font-size:1rem; }
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# HOME
# -----------------------------

def render_home():
    st.markdown(
        """
        <div class="app-hero">
          <div class="app-title">
            <span class="p1">Myra's</span>
            <span class="p2"> Study</span>
            <span class="p3"> App</span>
          </div>
          <div style="margin-top:8px;font-weight:700;">เลือกวิชาที่อยากติววันนี้ 🌷</div>
          <div class="subtle" style="margin-top:5px;">เรียนให้เข้าใจ • ฝึกทำโจทย์ • ทบทวนก่อนสอบ</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Subject grid 2 columns on mobile / 4 visual rows
    for row_start in range(0, len(SUBJECTS), 4):
        cols = st.columns(4)
        for col, subject in zip(cols, SUBJECTS[row_start:row_start+4]):
            icon, en, th, key, bg = subject
            with col:
                st.markdown(
                    f"""
                    <div class="subject-card" style="background:{bg}">
                      <div class="subject-icon">{icon}</div>
                      <div class="subject-en">{en}</div>
                      <div class="subject-th">{th}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if key == "science":
                    if st.button("เข้าเรียน", key=f"open_{key}", use_container_width=True):
                        st.session_state.page = "subject"
                        st.session_state.subject = "science"
                        st.session_state.unit_id = 1
                        st.session_state.section = "reading"
                        st.rerun()
                else:
                    st.button("เร็ว ๆ นี้", key=f"soon_{key}", use_container_width=True, disabled=True)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📝 ข้อสอบทบทวนทั้งหมด", use_container_width=True):
            st.session_state.page = "subject"
            st.session_state.subject = "science"
            st.session_state.section = "tests"
            st.rerun()
    with c2:
        if st.button(f"⭐ ข้อที่เคยผิด ({len(st.session_state.wrong_ids)})", use_container_width=True):
            st.session_state.page = "subject"
            st.session_state.subject = "science"
            st.session_state.section = "mistakes"
            st.rerun()

    st.markdown(
        """
        <div style="text-align:center;color:#8aa0b5;margin-top:24px;font-size:.9rem;">
          “ความพยายามเล็ก ๆ ในวันนี้ สร้างความเข้าใจที่ใหญ่ขึ้นได้เสมอ” 💗
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# SUBJECT NAVIGATION
# -----------------------------

def render_subject_header():
    top1, top2 = st.columns([1, 6])
    with top1:
        if st.button("←", key="back_home"):
            go_home()
    with top2:
        st.markdown("## 🌱 Science ป.1")

    # FIRST navigation + audio bar are one sticky block.
    # The audio toolbar sits immediately under บท 1–4, like the Reading app reference.
    with st.container(key="chapter_nav"):
        unit_cols = st.columns(4)
        for col, unit in zip(unit_cols, SCIENCE_UNITS):
            with col:
                label = f"{'✓ ' if st.session_state.unit_id == unit['id'] else ''}{unit['tab']}"
                if st.button(
                    label,
                    key=f"unit_{unit['id']}",
                    use_container_width=True,
                    type="primary" if st.session_state.unit_id == unit["id"] else "secondary",
                ):
                    st.session_state.unit_id = unit["id"]
                    st.session_state.section = "reading"
                    st.rerun()

        # Only show read-aloud controls while reading the lesson.
        if st.session_state.section == "reading":
            unit = get_unit(st.session_state.unit_id)
            plain_for_speech = (
                unit["reading"]
                .replace("#", "")
                .replace("*", "")
                .replace("-", " ")
            )
            read_aloud_button(plain_for_speech, f"sticky_unit{unit['id']}")

    # The pinned chapter/audio block is position:fixed, so reserve its space
    # before the normal page content starts.
    st.markdown('<div class="chapter-fixed-spacer"></div>', unsafe_allow_html=True)

    # Secondary navigation scrolls normally below the pinned block.
    st.markdown('<div class="section-strip">', unsafe_allow_html=True)
    sec_cols = st.columns(4)
    sections = [
        ("reading", "📖 สรุปบทเรียน"),
        ("practice", "✏️ แบบฝึกหัด"),
        ("tests", "📝 ข้อสอบทบทวน"),
        ("mistakes", f"⭐ ข้อที่เคยผิด ({len(st.session_state.wrong_ids)})"),
    ]
    for col, (key, label) in zip(sec_cols, sections):
        with col:
            if st.button(
                label,
                key=f"sec_{key}",
                use_container_width=True,
                type="primary" if st.session_state.section == key else "secondary",
            ):
                st.session_state.section = key
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# READING
# -----------------------------

def render_reading():
    unit = get_unit(st.session_state.unit_id)

    st.markdown(
        f"""
        <div class="big-panel">
          <div style="font-size:1.45rem;font-weight:900;color:#2b587d;">{unit['title']}</div>
          <div class="subtle" style="margin-top:6px;">{unit['subtitle']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="reading-card">', unsafe_allow_html=True)
    st.markdown(unit["reading"])
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✏️ ทำแบบฝึกหัดบทนี้", use_container_width=True):
            st.session_state.section = "practice"
            st.rerun()
    with c2:
        if st.button("📝 ไปข้อสอบทบทวน", use_container_width=True):
            st.session_state.section = "tests"
            st.rerun()

# -----------------------------
# PRACTICE
# -----------------------------

def render_practice():
    unit = get_unit(st.session_state.unit_id)
    st.markdown(f"### ✏️ แบบฝึกหัด — {unit['title']}")
    st.caption("ตอบแล้วจะเห็นเฉลยทันที ข้อที่ตอบผิดจะถูกเก็บไว้ใน “ข้อที่เคยผิด”")

    for idx, q in enumerate(unit["practice"], start=1):
        st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
        st.markdown(f"**ข้อ {idx} / {len(unit['practice'])}**")
        st.markdown(f"#### {q['question']}")

        state_key = f"practice_answer_{q['id']}"
        if state_key not in st.session_state:
            st.session_state[state_key] = None

        choice_cols = st.columns(len(q["choices"]))
        for col, choice in zip(choice_cols, q["choices"]):
            with col:
                if st.button(
                    choice,
                    key=f"{q['id']}_{choice}",
                    use_container_width=True,
                    disabled=st.session_state[state_key] is not None,
                ):
                    st.session_state[state_key] = choice
                    st.session_state.answered[q["id"]] = choice
                    if choice != q["answer"]:
                        st.session_state.wrong_ids.add(q["id"])
                    st.rerun()

        answer = st.session_state[state_key]
        if answer is not None:
            if answer == q["answer"]:
                st.markdown(
                    f'<div class="good"><b>✅ ถูกต้อง!</b><br>{q["explain"]}</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f'<div class="bad"><b>❌ ยังไม่ใช่</b><br>คำตอบที่ถูกต้องคือ <b>{q["answer"]}</b><br>{q["explain"]}</div>',
                    unsafe_allow_html=True,
                )
                if st.button("ลองข้อนี้ใหม่", key=f"retry_practice_{q['id']}"):
                    st.session_state[state_key] = None
                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    if st.button("📝 ทำข้อสอบทบทวนบทนี้", use_container_width=True):
        start_test("unit", st.session_state.unit_id)
        st.session_state.section = "tests"
        st.rerun()

# -----------------------------
# TESTS
# -----------------------------

def render_test_setup():
    unit = get_unit(st.session_state.unit_id)
    st.markdown("### 📝 ข้อสอบทบทวน")
    st.caption("โหมดข้อสอบจะไม่เฉลยทีละข้อ เพื่อให้เหมือนทำข้อสอบจริงมากขึ้น")

    cards = [
        ("📘 ทบทวนรายบท", f"เฉพาะ {unit['title']}", "unit"),
        ("📚 ทบทวนทั้งเล่ม", "สุ่มคำถามจากทั้ง 4 หน่วย", "book"),
        ("🏆 ก่อนสอบ", "แบบทดสอบรวม 15 ข้อ", "exam"),
    ]

    for title, subtitle, mode in cards:
        st.markdown(
            f"""
            <div class="big-panel" style="margin-bottom:10px;">
              <div style="font-size:1.1rem;font-weight:900;">{title}</div>
              <div class="subtle">{subtitle}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button(f"เริ่ม {title}", key=f"start_{mode}", use_container_width=True):
            start_test(mode, st.session_state.unit_id)
            st.rerun()

    if st.session_state.wrong_ids:
        st.markdown("---")
        if st.button(
            f"⭐ ทำเฉพาะข้อที่เคยผิด ({len(st.session_state.wrong_ids)} ข้อ)",
            use_container_width=True
        ):
            start_test("wrong")
            st.rerun()

def render_active_test():
    questions = st.session_state.test_questions

    if st.session_state.test_finished:
        render_test_result()
        return

    if not questions:
        render_test_setup()
        return

    idx = st.session_state.test_index
    if idx >= len(questions):
        st.session_state.test_finished = True
        st.rerun()

    q = questions[idx]
    progress = (idx + 1) / len(questions)
    st.progress(progress)
    st.markdown(f"**ข้อ {idx + 1} / {len(questions)}**")
    st.markdown(f"### {q['question']}")

    current_answer = st.session_state.test_answers.get(q["id"])
    choice_cols = st.columns(len(q["choices"]))
    for col, choice in zip(choice_cols, q["choices"]):
        with col:
            if st.button(
                choice,
                key=f"test_{idx}_{q['id']}_{choice}",
                use_container_width=True,
                disabled=current_answer is not None,
            ):
                save_test_answer(q, choice)
                st.rerun()

    current_answer = st.session_state.test_answers.get(q["id"])
    if current_answer is not None:
        st.info(f"เลือกคำตอบแล้ว: **{current_answer}**")
        if st.button(
            "ส่งคำตอบและไปข้อต่อไป →",
            key=f"next_test_{idx}",
            use_container_width=True
        ):
            st.session_state.test_index += 1
            if st.session_state.test_index >= len(questions):
                st.session_state.test_finished = True
            st.rerun()

def render_test_result():
    questions = st.session_state.test_questions

    if not questions:
        st.info("ยังไม่มีข้อสำหรับโหมดนี้ค่ะ")
        if st.button("กลับหน้าข้อสอบ", use_container_width=True):
            st.session_state.test_questions = []
            st.session_state.test_finished = False
            st.rerun()
        return

    correct = 0
    for q in questions:
        if st.session_state.test_answers.get(q["id"]) == q["answer"]:
            correct += 1

    score = round(correct / len(questions) * 100)
    st.markdown(
        f"""
        <div class="app-hero">
          <div style="font-size:2.2rem;">🎉</div>
          <div style="font-size:1.65rem;font-weight:900;">เก่งมาก Myra!</div>
          <div style="font-size:2rem;font-weight:900;color:#55a97e;margin-top:8px;">{correct} / {len(questions)}</div>
          <div class="subtle">คะแนน {score}%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### เฉลย")
    for i, q in enumerate(questions, start=1):
        user_answer = st.session_state.test_answers.get(q["id"])
        is_correct = user_answer == q["answer"]
        with st.expander(f"{'✅' if is_correct else '❌'} ข้อ {i}: {q['question']}"):
            st.write(f"คำตอบของหนู: **{user_answer or '-'}**")
            st.write(f"คำตอบที่ถูกต้อง: **{q['answer']}**")
            st.write(q["explain"])

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔁 ทำชุดใหม่", use_container_width=True):
            mode = st.session_state.test_mode
            start_test(mode, st.session_state.unit_id)
            st.rerun()
    with c2:
        if st.button("⭐ ไปทบทวนข้อที่ผิด", use_container_width=True):
            st.session_state.test_questions = []
            st.session_state.test_finished = False
            st.session_state.section = "mistakes"
            st.rerun()

def render_tests():
    if st.session_state.test_questions or st.session_state.test_finished:
        render_active_test()
    else:
        render_test_setup()

# -----------------------------
# MISTAKES
# -----------------------------

def render_mistakes():
    st.markdown("### ⭐ ข้อที่เคยผิด")
    st.caption("ทบทวนเฉพาะจุดที่ยังสับสน พอตอบถูกในโหมดทบทวน ระบบจะนำข้อนั้นออกจากรายการ")

    wrong_questions = [
        question_by_id(qid)
        for qid in list(st.session_state.wrong_ids)
        if question_by_id(qid) is not None
    ]

    if not wrong_questions:
        st.success("ตอนนี้ไม่มีข้อที่ต้องทบทวนค่ะ 🎉")
        st.markdown("ทำแบบฝึกหัดหรือข้อสอบเพิ่มเติม แล้วข้อที่ตอบผิดจะมาอยู่ตรงนี้อัตโนมัติ")
        return

    for i, q in enumerate(wrong_questions, start=1):
        st.markdown(
            f"""
            <div class="mistake-card">
              <b>{i}. {q['question']}</b><br>
              <span class="subtle">หน่วย: {q['unit_title']}</span><br>
              <span style="color:#4d7a62;">คำตอบที่ถูกต้อง: <b>{q['answer']}</b></span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    if st.button(
        f"🔁 เริ่มทบทวน {len(wrong_questions)} ข้อ",
        use_container_width=True
    ):
        start_test("wrong")
        st.session_state.section = "tests"
        st.rerun()

# -----------------------------
# APP
# -----------------------------

if st.session_state.page == "home":
    render_home()

elif st.session_state.page == "subject" and st.session_state.subject == "science":
    # Keep header/nav and all page content inside one tall parent.
    # This allows the nested chapter_nav block to remain sticky during scrolling.
    with st.container(key="science_page"):
        render_subject_header()

        if st.session_state.section == "reading":
            render_reading()
        elif st.session_state.section == "practice":
            render_practice()
        elif st.session_state.section == "tests":
            render_tests()
        elif st.session_state.section == "mistakes":
            render_mistakes()

else:
    render_home()
