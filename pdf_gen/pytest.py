from fpdf_qpaper import QPaper

pdf = QPaper(orientation = 'P', unit = 'mm', format='A4')
pdf.date = '15.08.2023'
pdf.marks = 20
pdf.clss = 6
pdf.add_page()

q_paper_dict = {
    0:{
        "q_mark": 2,
        "q_nos": 10,
        "q_header_txt": "Answer the following questions"
        },
    1:{
        "q_mark": 3,
        "q_nos": 10,
        "q_header_txt": "Answer the following questions"
        }
}

def setQuestionHeader(q_idx, q_header_txt, q_nos, q_mark):
    pdf.q_header_font()
    pdf.cell(200 // 2, pdf.cw, "{}. {}:".format(q_idx, q_header_txt), ln=0, align='L')
    pdf.cell(200 // 2 + 3, pdf.cw, "{}x{}={} Marks".format(q_nos, q_mark, q_nos * q_mark), ln=1, align='R')
    pdf.ln(2)

for i in range(len(q_paper_dict.keys())):
    setQuestionHeader(i+1,q_paper_dict[i]["q_header_txt"],q_paper_dict[i]["q_nos"],q_paper_dict[i]["q_mark"])

pdf.txt_font()

pdf.output("question_paper.pdf")
