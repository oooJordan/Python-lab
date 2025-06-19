#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def media_studente(stud_code, dbsize):
    with open(f"{dbsize}_exams.json", encoding='utf8') as exams_file:
        exams = json.load(exams_file)

    esami_dict = {esame["exam_code"]: esame for esame in exams}

    esami_sostenuti = [esame for exam_code, esame in esami_dict.items() if esame["stud_code"] == stud_code]

    somma_voti = sum(exam["grade"] for exam in esami_sostenuti)
    numero_esami = len(esami_sostenuti)
    if numero_esami == 0:
        return 0
    else:
        return round(somma_voti / numero_esami,2)


def media_corso(course_code, dbsize):

    with open(f"{dbsize}_exams.json", encoding='utf8') as exams_file:
        exams = json.load(exams_file)


    esami_dict = {esame["exam_code"]: esame for esame in exams}

    esami_corso = {exam_code: esame for exam_code, esame in esami_dict.items() if esame["course_code"] == course_code}

    voti_totali = 0.0
    num_esami = len(esami_corso)
    for esame in esami_corso.values():
        voti_totali += esame["grade"]

    if num_esami > 0:
        return round(voti_totali / num_esami, 2)
    else:
        return 0


def media_docente(teach_code, dbsize):
    with open(f"{dbsize}_courses.json", encoding='utf8') as courses_file:
        courses = json.load(courses_file)
    with open(f"{dbsize}_exams.json", encoding='utf8') as exams_file:
        exams = json.load(exams_file)

    corsi_dict = {corso["course_code"]: corso for corso in courses}
    
    esami_dict = {esame["exam_code"]: esame for esame in exams}
    corsi_docente = {course_code: corso for course_code, corso in corsi_dict.items() if corso["teach_code"] == teach_code}

    voti_totali = 0.0
    num_esami = 0
    for course_code, corso in corsi_docente.items():
        esami_corso = [exam_code for exam_code in esami_dict if esami_dict[exam_code]["course_code"] == course_code]
        for exam_code in esami_corso:
            voti_totali += esami_dict[exam_code]["grade"]
        num_esami += len(esami_corso)

    if num_esami > 0:
        return round(voti_totali / num_esami, 2)
    else:
        return 0


def studenti_brillanti(dbsize):
    with open(f"{dbsize}_students.json", encoding='utf8') as students_file:
        students = json.load(students_file)

    
    voti_medi = {}
    for student in students:
        stud_code = student["stud_code"]
        voto_medio = round(media_studente(stud_code, dbsize), 2)
        voti_medi[stud_code] = voto_medio

    
    brillanti_dict = {stud_code: voto_medio for stud_code, voto_medio in voti_medi.items() if voto_medio >= 28}

    
    brillanti = sorted(brillanti_dict, key=lambda x: (-brillanti_dict[x], *[s["stud_surname"] for s in students if s["stud_code"] == x], x))

    return brillanti



def stampa_verbale(exam_code, dbsize, fileout):
  with open(f"{dbsize}_exams.json", encoding='utf8') as exams_file:
    exams = json.load(exams_file)
  with open(f"{dbsize}_students.json", encoding='utf8') as students_file:
    studenti= json.load(students_file)
  with open (f"{dbsize}_teachers.json", encoding='utf8') as teacher_file:
      prof=json.load(teacher_file)
  with open(f"{dbsize}_courses.json", encoding='utf8') as courses_file:
      courses = json.load(courses_file)
      
  exam = next(exam for exam in exams if exam["exam_code"] == exam_code)
  student = next(student for student in studenti if student["stud_code"] == exam["stud_code"])
  course = next(course for course in courses if course["course_code"] == exam["course_code"])
  teacher = next(teacher for teacher in prof if teacher["teach_code"] == course["teach_code"])

  exam_string = f"Lo studente {student['stud_name']} {student['stud_surname']}, matricola {student['stud_code']}, ha sostenuto in data {exam['date']} l'esame di {course['course_name']} con il docente {teacher['teach_name']} {teacher['teach_surname']} con votazione {exam['grade']}."

  with open(fileout, "w", encoding='utf-8') as f:
        f.write(exam_string)
  return exam["grade"]


def stampa_esami_sostenuti(stud_code, dbsize, fileout):
    with open(f"{dbsize}_exams.json", encoding='utf8') as exams_file:
        exams = json.load(exams_file)
    with open(f"{dbsize}_students.json", encoding='utf8') as students_file:
        students = json.load(students_file)
    with open(f"{dbsize}_courses.json", encoding='utf8') as courses_file:
        courses = json.load(courses_file)
        
    exams_dict = {esame["exam_code"]: esame for esame in exams}
    students_dict = {student["stud_code"]: student for student in students}
    courses_dict = {course["course_code"]: course for course in courses}

    
    esami_sostenuti = [{**exams_dict[exam_code], **students_dict[exams_dict[exam_code]["stud_code"]], **courses_dict[exams_dict[exam_code]["course_code"]], "grade": int(exams_dict[exam_code]["grade"])} 
                       for exam_code in exams_dict if exams_dict[exam_code]["stud_code"] == stud_code]

    
    esami_sostenuti = sorted(esami_sostenuti, key=lambda x: (x["date"], x["course_code"], x["stud_surname"], x["stud_name"]))

    max_course_name_len = max(len(esame["course_name"]) for esame in esami_sostenuti)
    
    with open(fileout, "w", encoding='utf8') as f:
        f.write(f"Esami sostenuti dallo studente {esami_sostenuti[0]['stud_surname']} {esami_sostenuti[0]['stud_name']}, matricola {stud_code}\n")
        for esame in esami_sostenuti:
            course_name = esame['course_name']
            f.write(f"{course_name:<{max_course_name_len}}\t{esame['date']}\t{esame['grade']}\n")

    return len(esami_sostenuti)
    


def stampa_studenti_brillanti(dbsize, fileout):
    with open(f"{dbsize}_students.json", encoding='utf8') as students_file:
        students = json.load(students_file)

    voti_medi = {}
    for studente in students:
        voti_medi[studente["stud_code"]] = media_studente(studente["stud_code"], dbsize)
    

    studenti_brillanti = []
    for studente in students:
        if voti_medi[studente["stud_code"]] >= 28:
            studenti_brillanti.append((studente["stud_surname"], studente["stud_name"], studente["stud_code"], voti_medi[studente["stud_code"]]))

 
    studenti_brillanti.sort(key=lambda s: (-s[3], s[0], s[1],s[2]))
    
    
    lunghezza_massima = max(len(studente[0]+studente[1]) for studente in studenti_brillanti)

    
    with open(fileout, "w", encoding='utf8') as f:
        for studente in studenti_brillanti:
            f.write('{:<{}}\t{:>}\n'.format(studente[0]+ ' ' + studente[1], lunghezza_massima+1, studente[3]))

    return len(studenti_brillanti)
