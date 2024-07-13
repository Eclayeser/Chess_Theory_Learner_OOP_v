import time
class OpeningsFileHandler:
    def __init__(self, givenName):
        self.file = givenName
        
    def find_opening(self, file_name):
        #must return dictionary in form: 
        #chess_opening_beta = {"player":"white", "opening":"Bird's", "main_variation":"From's Gambit", "side_variations":["Variation #1", "Variation #2"], "Variation #1": {"white": ["f2|f4", "f4:e5", "e5:d6"], "black": ["e7|e5", "d7|d6"]}, "Variation #2": {"white": ["f2|f4", "f4:e5", "d2|d4"], "black": ["e7|e5", "d7|d5"]}}
        pass
        
    
    def open_file_to_read(self):
        self.file_open = open(self.file, "r")
    
    def close_file(self):
        self.file_open.close()  

    def separate_openings(self):
        self.open_file_to_read()
        all_data = self.file_open.read()
        self.close_file()

        traversed = False
        work_data = all_data
        openings_list = []
        while traversed == False:
            pos_1, pos_2 = work_data.find("{"), work_data.find("}")
            if pos_1 != -1 and pos_2 != -1:
                openings_list.append(work_data[pos_1+1:pos_2])
                work_data = work_data[pos_2+1:]
            else:
                traversed = True

        return openings_list

    def search_for_name(self, name, list):
        found_list_item = False
        traversed_list = False
        op_num = 0 
        while found_list_item == False and traversed_list == False:
            #list traversed
            if op_num == len(list):
                traversed_list = True

            #list not traversed
            else:
                single_op = list[op_num]

                pos_turn_sign_1 = single_op.find("~")
                pos_turn_sign_2 = single_op[pos_turn_sign_1+1:].find("~")
                for_who = single_op[pos_turn_sign_1+1:][:pos_turn_sign_2]

                traverse_single = False
                found_var = False

                check_op_name = single_op[list[op_num].find("[")+1:list[op_num].find("]")]
                work_op = single_op

                while traverse_single == False and found_var == False:
                    #print("-------------------------")
                    #print(work_op)
                    #time.sleep(2)
                    pos_first_forwsl = work_op.find("/")
                    pos_first_backsl = work_op.find("\\")

                    #traversed
                    if pos_first_backsl == -1 and pos_first_forwsl == -1:
                        traverse_single = True
                    
                    #not fully traversed
                    else:
                        check_var_name = work_op[pos_first_forwsl+1:pos_first_backsl]
                        full_check_name = (check_op_name + ": " +check_var_name).lower()
                        #print(full_check_name)
                        
                        #if op and var found
                        if full_check_name == name:
                            found_var = True
                            text_left = work_op[pos_first_backsl+1:]

                            pos_next_backslash = text_left.find("/")

                            #print(text_left)

                            if pos_next_backslash == -1:
                                searched_op = text_left
                            else:
                                searched_op = text_left[:pos_next_backslash]

                        #if not found
                        else:
                            work_op = work_op[pos_first_backsl+1:]

                #if found            
                if found_var == True:
                    found_list_item = True

                #not found
                else:
                    op_num += 1

        if found_list_item == True:
            list_result = [for_who, check_op_name, check_var_name, searched_op]
            return list_result
        
        elif traversed_list == True:
            return False

    def split_variations(self, text_data):
        #output: list of var names, list of white moves, list of black moves
        vars_list = []
        white_moves = []
        black_moves = []
        all_moves = []

        work_data = text_data
        traversed_vars = False

        while traversed_vars == False:

            pos_open_br, pos_closed_br = work_data.find("("), work_data.find(")")

            #available vars
            if pos_open_br != -1 and pos_closed_br != -1:
                new_variation = work_data[pos_open_br+1:pos_closed_br]
                vars_list.append(new_variation)

                
                
                work_data = work_data[pos_closed_br+1:]
                """
                next_br = work_data.find("(")
                moves = work_data[:next_br]
                moves_traversed = False
                move_num = 1
                moves_left = moves
                while moves_traversed == False:
                    print("-----------------")
                    print(moves_left)
                    time.sleep(2)
                    move_num_str = str(move_num)+"."
                    move_num_str_next = str(move_num+1)+"."
                    if move_num_str in moves_left:
                        p_1 = moves_left.find(move_num_str)
                        p_2 = moves_left.find(move_num_str_next)
                        double_move = moves_left[p_1+2:p_2]

                        lim_1 = double_move.find(" ")
                        white_moves.append(double_move[:lim_1])

                        black_move = double_move[lim_1+1:]
                        lim_2 = black_move.find(" ")
                        black_moves.append(black_move[:lim_2])

                        moves_left = moves_left[p_2:]

               

                    else:
                        moves_traversed = True

                """  


            #traversed vars
            else:
                traversed_vars = True

        return vars_list#, white_moves, black_moves

            


openings_database = OpeningsFileHandler("openings.txt")
list_result = openings_database.search_for_name("bird's: from's gambit", openings_database.separate_openings())
print(openings_database.split_variations(list_result[3]))