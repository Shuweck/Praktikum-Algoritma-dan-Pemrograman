grade = []

print('--- Nilai Tertinggi? ---')

while True:
    score = (input('Masukkan nilai ("stop" untuk berhenti): '))
    if score == 'stop':
        break
    grade.append(int(score))

print('Nilai tertinggi yang suneo dapatkan pada UTS kali ini: ',(max(grade)))