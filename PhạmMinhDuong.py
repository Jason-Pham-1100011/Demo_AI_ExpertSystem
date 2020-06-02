# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:02:26 2020

@author: PHẠM MINH DƯƠNG - 51702081
"""

from sympy.logic.boolalg import to_cnf

""" ============================== AI ENGINEER ================================ """

global clause_variable_list

def negative_clause(clause):
    if "|" in clause:
        clause_variables = clause.split("|")
        for clause_variable in range(len(clause_variables)):
            if "~" in clause_variables [clause_variable]:
                clause_variables [clause_variable] = clause_variables [clause_variable].lstrip("~")
            else:
                clause_variables [clause_variable] = "~" + clause_variables [clause_variable]
                
        join = "|"
        return join.join(clause_variables)
    else:
        if "~" in clause:
            clause = clause.lstrip("~")
        else:
            clause = "~" + clause
        return clause
    
def is_opposition(clause1, clause2):
    if (negative_clause(clause1) == clause2) or (clause1 == negative_clause(clause2)):
        return True
    return False
    
def check_opposition_clause_KB(KB):
    for i in range(len(KB) - 1):
        for j in range(i + 1 ,len(KB)):
            if is_opposition(KB[i],KB[j]):
                return True
    return False

def choose_clause_variable():
    if len( clause_variable_list ) > 0:
        out_clause_variable = clause_variable_list.pop()
        return out_clause_variable
    else:
        return None

def select_clauses_by_variable(variable,KB):
    out_clauses_list = []
    for clause in KB:
        if variable in clause:
            out_clauses_list.append(clause)
    
    return out_clauses_list

def factoring(clause):
    variables = clause.split("|")
    variables = list( dict.fromkeys(variables))
    join = "|"
    return join.join(variables)

def res(clause1, clause2,cl_var):

    remove_blog = []
    out_new_clause = []
    is_have_change = False
    
    if "|" in clause1:
        cl_variables1 = clause1.split("|")
        
    else:
        cl_variables1 = [clause1]
        
    if "|" in clause2:
        cl_variables2 = clause2.split("|")

    else:
        cl_variables2 = [clause2]

    for i in range( len(cl_variables1) ):
        for j in range( len(cl_variables2) ):
            if (cl_var in cl_variables1[i] and cl_var in cl_variables2[j]) and is_opposition(cl_variables1[i],cl_variables2[j]):
                remove_blog.append([cl_variables1[i],cl_variables2[j]])
                is_have_change = True
    if is_have_change:
        for rm_el in remove_blog:
            cl_variables1.remove(rm_el[0])
            cl_variables2.remove(rm_el[1])
            
        out_new_clause.extend(cl_variables1)
        out_new_clause.extend(cl_variables2)
        join = "|"
        return factoring(join.join(out_new_clause))
    else:
        return None
        
def resolution(clauses,cl_var,KB):
    n_clauses = []
    for i in range (len(clauses) - 1):
        for j in range (i+1,len(clauses)):
            if res(clauses[i],clauses[j],cl_var) != None:
                n_clause = res(clauses[i],clauses[j],cl_var)
                n_clauses.append(n_clause)
                
    if len(n_clauses) > 0:            
        for clause in clauses:
            KB.remove(clause)
            
        KB.extend(n_clauses)
    return KB

def robinson_davisputman(KB):
    print("====================================================================")
    print("ALGORITHM: ROBINSON DAVISPUTMAN ")
    print("AI ENGINEER RESOLUTING...")    
    print("KB is received: ",KB)
    
    while (len(KB)>0):
        if check_opposition_clause_KB(KB):
            return True
        else:
            clause_variable = choose_clause_variable()
            print(clause_variable)
            if clause_variable != None:
               clauses_by_variable = select_clauses_by_variable(clause_variable,KB)
               print(clauses_by_variable)
               KB = resolution(clauses_by_variable,clause_variable, KB)
               print("Update KB >>>",KB)
            else:
                return False
    return True

"""=====================================EXPERT SYSTEM======================================="""

def survey():
    '''
    Mô tả mệnh đề
    //IT: I
    Thích công nghệ : C
    Thích giải toán và logic tốt: T
    Thích kiên nhẫn chịu khó tỉ mỉ: K
    Tự giác ham học hỏi cái mới: H
    Thích học một kiến thức áp dụng mãi mãi : N
    Không muốn over night: O
    Làm việc nhóm: W
    Có thể ngồi trên máy tính thời gian dài: U

    
    //DESIGN: 
    Thích sáng tạo: S
    Thích mỹ thuật, hội họa: M
    Tự giác học hỏi cái mới: H
    Giao tiếp tốt: A
    Thích gặp mặt nhiều người: B
    
    //KINH DOANH:
    Giao tiếp tốt: A
    Thích gặp mặt nhiều người: B
    Diễn đạt đốt: D
    Thích kinh doanh mua bán: E
    Kỹ năng thuyết phục tốt:  F
    
    //DU LỊCH:
    Giao tiếp tốt: A
    Thích gặp mặt nhiều người: B
    Diễn đạt đốt: D        
    Ghi nhớ tốt : G
    Thích đi nhiều nơi: L
    '''
    print ("===================================================================")
    print ("================== KHẢO SÁT THU THẬP THÔNG TIN ====================")
    print()
    print ("Trả lời các câu hỏi sau bằng kí tự C (Có) , K (Không): ")
    print ()
    
    survey_answer_clause_list = []
    survey_question_dict = {
                            "C": "Bạn có thích công nghệ hay không?",
                            "T": "Bạn có thích giải toán hay có khả năng về tư duy logic tốt?",
                            "K": "Bạn có tính kiên nhẫn, tỉ mỉ hay không?",
                            "H": "Bạn có khả năng tự tìm hiểu, học hỏi cái mới hay không?",
                            "O": "Bạn có phải là kiểu người KHÔNG thể chịu áp lực làm việc qua đêm hay không?",
                            "W": "Bạn có khả năng làm việc nhóm hay không?",
                            "U": "Bạn có thể dành thời gian nhiều để làm việc trên máy tính hay không?",
                            "S": "Bạn có thích hoặc có khả năng sáng tạo hay không?",
                            "M": "Bạn có đam mê hoặc có khả năng về mỹ thuật, hội họa hay không?",
                            "A": "Bạn có thích giao tiếp hoặc có khả năng giao tiếp hay không?",
                            "B": "Bạn có thích gặp mặt nhiều người hay không?",
                            "D": "Bạn có khả năng diễn đạt tốt hay không?",
                            "E": "Bạn có đam mê hoặc khả năng kinh doanh mua bán hay không?",
                            "F": "Bạn có khả năng tốt về thuyết phục người khác hay không?",
                            "G": "Bạn có khả năng ghi nhớ tốt hay không?",
                            "L": "Bạn có thích công việc của mình phải di chuyển du lịch nhiều nơi hay không?"
                            }
    
    for question_clause in survey_question_dict:
        print(survey_question_dict[question_clause])
        answer = input("Câu trả lời (C/K): ")
        if answer == "C":
            survey_answer_clause_list.append(question_clause)
        
            
    print("Kết quả khảo sát: ",survey_answer_clause_list)
    print("====================================================================")
    print()
    return survey_answer_clause_list
def expert_sys():
    
    '''
    Knowledge Base:
    //IT: I
    (C & U & T & K & H & W & ~O) >> I
    N >> ~H
    (~C| O) >> ~U
    
    //DESIGN: P
    (S & M & H & A & B) >> P
    
    //KINH DOANH: Q
    (A & B & D & E & F) >> Q
    
    //DU LICH: V
    (A & B & D & G & L) >> V
    
    ~B >> ~A
    '''
    
    '''Surey Result Base'''
    RSB = survey()
    
    ''' Excute check job'''
    print_result([check_it(RSB),check_design(RSB),check_marketing(RSB),check_travel(RSB)])

def print_result(result_list):
    '''
    0: IT
    1: DESIGN
    2: MARKETING
    3: TRAVEL
    
    '''
    print ("===================================================================")
    print ("========================= KẾT QUẢ SUY ĐOÁN ========================")
    print ()
    print ("LỜI KHUYÊN DÀNH CHO BẠN: ")
    print ()
    
    job_list = ["Các ngành về kỷ thuật như Công nghệ thông tin.", 
                "Các ngành thiết kế đồ họa.", 
                "Các ngành kinh tế, kinh doanh.",
                "Các ngành du lịch."]
    
    for i in range( len(result_list)):
        if result_list[i]:
            print ("Bạn phù hợp với: " + job_list[i])
        else:
            print ("Bạn không phù hợp với: " + job_list[i])

    print("====================================================================")

def check_marketing(RSB):
    
    print("DATA INFORMATION IN FUNTION: CHECK_MARKETING")
    global clause_variable_list
    
    input_clauses = ["A","B","D","E","F"]
    input_KB = ["(A & B & D & E & F) >> Q"]
    prove_clause = "Q"
    KB = [] #Knowledge Base
    clause_variable_list = []
    
    clause_variable_list.extend(input_clauses)
    clause_variable_list.extend(prove_clause)

    for clause in input_KB:
        KB.extend(convert_to_cnf(clause.lower()))    

    for clause in input_clauses:
        if clause not in RSB:
            input_clauses[input_clauses.index(clause)] = negative_clause(clause)
    
    print("INPUT CLAUSES: ",input_clauses)
    
    KB.extend(input_clauses)
    KB.append(negative_clause(prove_clause))
    
    print ("CLAUSES VARIABLES:", clause_variable_list)
    print ("KB IN FUNTION: ", KB)
    
    result = robinson_davisputman(KB)
    
    print("RESULT: ",result)
    return result
    
def check_travel(RSB):
    
    print("DATA INFORMATION IN FUNTION: CHECK_TRAVEL")
    
    global clause_variable_list
    
    input_clauses = ["A","B","D","G","L"]
    input_KB = ["(A & B & D & G & L) >> V"]
    prove_clause = "V"
    KB = [] #Knowledge Base
    clause_variable_list = []
    
    clause_variable_list.extend(input_clauses)
    clause_variable_list.extend(prove_clause)

    for clause in input_KB:
        KB.extend(convert_to_cnf(clause.lower()))    

    for clause in input_clauses:
        if clause not in RSB:
            input_clauses[input_clauses.index(clause)] = negative_clause(clause)
    
    print("INPUT CLAUSES: ",input_clauses)
    
    KB.extend(input_clauses)
    KB.append(negative_clause(prove_clause))
    
    print ("CLAUSES VARIABLES:", clause_variable_list)
    print ("KB IN FUNTION: ", KB)
    
    result = robinson_davisputman(KB)
    
    print("RESULT: ",result)
    return result

def check_design(RSB):
    
    print("DATA INFORMATION IN FUNTION: CHECK_DESIGN")
    
    global clause_variable_list
    
    input_clauses = ["S","M","H","A","B"]
    input_KB = ["(S & M & H & A & B) >> P"]
    
    prove_clause = "P"
    KB = [] #Knowledge Base
    clause_variable_list = []
    
    clause_variable_list.extend(input_clauses)
    clause_variable_list.extend(prove_clause)

    for clause in input_KB:
        KB.extend(convert_to_cnf(clause.lower()))    

    for clause in input_clauses:
        if clause not in RSB:
            input_clauses[input_clauses.index(clause)] = negative_clause(clause)
    
    print("INPUT CLAUSES: ",input_clauses)
    
    KB.extend(input_clauses)
    KB.append(negative_clause(prove_clause))
    
    print ("CLAUSES VARIABLES:", clause_variable_list)
    print ("KB IN FUNTION: ", KB)
    
    result = robinson_davisputman(KB)
    
    print("RESULT: ",result)
    return result


def check_it(RSB):
    
    print("DATA INFORMATION IN FUNTION: CHECK_IT")

    global clause_variable_list
    
    input_clauses = ["C","U","T","K","H","W","O"]
    input_KB = ["(C & U & T & K & H & W & ~O) >> I"]
    prove_clause = "I"
    KB = [] #Knowledge Base
    clause_variable_list = []
    
    clause_variable_list.extend(input_clauses)
    clause_variable_list.extend(prove_clause)

    for clause in input_KB:
        KB.extend(convert_to_cnf(clause.lower()))    

    for clause in input_clauses:
        if clause not in RSB:
            input_clauses[input_clauses.index(clause)] = negative_clause(clause)
    
    print("INPUT CLAUSES: ",input_clauses)
    
    KB.extend(input_clauses)
    KB.append(negative_clause(prove_clause))
    
    print ("CLAUSES VARIABLES:", clause_variable_list)
    print ("KB IN FUNTION: ", KB)
    
    result = robinson_davisputman(KB)
    
    print("RESULT: ",result)
    return result

def convert_to_cnf(clause):
    out_clause =  repr(to_cnf(clause))
    
    out_clause = out_clause.replace("(","").replace(")","").replace(" ","")
    out_clause = out_clause.upper()
    if "&" in out_clause:
       out_clause = out_clause.split("&")
       return out_clause
    return [out_clause]


if __name__ == "__main__":
    expert_sys()
    
    
#print(factoring("A|A"))
#KB = ["~S|D|N","~S|~D|L","~S|~L|~E","S","E","~S|~N"]
#print(select_clauses_by_variable("B",KB))

#print(resolution(select_clauses_by_variable("C",KB),KB))

#out  = robinson_davisputman(KB)
#print(out)



#in_KB = ["(C & U & T & K & H & W & ~O) >> I","(N|K) >> ~H"]
#out_KB = []
#
#for clause in in_KB:
#    print(clause, ":" ,convert_to_cnf(clause.lower()))
#    out_KB.extend(convert_to_cnf(clause.lower()))
#
#print(out_KB)



#print( convert_to_cnf(str("(C & U & T & K & H & W & ~O) >> I").lower()) )
#print(is_opposition('~C','C'))