
class OpeningsFileHandler:
    def __init__(self, givenName):
        self.file = givenName
   
    def open_file_to_read(self):
        self.file_open = open(self.file, "r")
    
    def close_file(self):
        self.file_open.close()  

    def separate_openings(self):
        #produces list of general openings separated by { and }
        self.open_file_to_read()
        all_data = self.file_open.read()
        self.close_file()

        pos_1 = all_data.find("///")
        pos_2 = all_data[pos_1+3:].find("///") + 3
        all_data = all_data[pos_2+3:]

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

    def search_for_name(self, given_name, list):
        #searches for a particular opening in the list to identify if exists
        def identify_perspective(op):
            pos_1 = op.find("~")
            pos_2 = op[pos_1+1:].find("~")
            colour = op[pos_1+1:][:pos_2]
            if "White" in colour:
                colour_return = "white"
            elif "Black" in colour:
                colour_return = "black"
            return colour_return

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

                for_who = identify_perspective(single_op)

                traverse_single = False
                found_var = False

                check_op_name = single_op[list[op_num].find("[")+1:list[op_num].find("]")]
                work_op = single_op

                while traverse_single == False and found_var == False:
                    pos_first_forwsl = work_op.find("/")
                    pos_first_backsl = work_op.find("\\")

                    #traversed
                    if pos_first_backsl == -1 and pos_first_forwsl == -1:
                        traverse_single = True
                    
                    #not fully traversed
                    else:
                        check_var_name = work_op[pos_first_forwsl+1:pos_first_backsl]
                        full_check_name = (check_op_name + ": " +check_var_name).lower()
                        
                        
                        #if op and var found
                        if full_check_name == given_name:
                            found_var = True
                            #moves in text type
                            text_left = work_op[pos_first_backsl+1:]

                            pos_next_backslash = text_left.find("/")
                            #variation in the opening
                            if pos_next_backslash == -1:
                                searched_op = text_left
                            #there are more variations not traverse -> discard those
                            else:
                                searched_op = text_left[:pos_next_backslash]

                        #if not found
                        else:
                            work_op = work_op[pos_first_backsl+1:]

                #if op and var found            
                if found_var == True:
                    found_list_item = True

                #not found
                else:
                    op_num += 1
        
        #if particular opening was found -> return details
        if found_list_item == True:
            list_result = [for_who, check_op_name, check_var_name, searched_op]
            return list_result
        
        #wasn't found -> return False for each detail
        elif traversed_list == True:
            return False, False, False, False,

    def split_variations(self, text_data):
        #takes an opening and its main variation to produce list of side vars and respective white and black moves for each side var
        #output: list of var names, dictinary of list of white moves and list of black moves
        def produce_lists_of_moves_for_side_var(moves_to_traverse):
            white_moves_local_list = []
            black_moves_local_list = []
            moves_traversed = False
            move_num = 1
            moves_left = moves_to_traverse

            while moves_traversed == False:
                    
                move_num_str = str(move_num)+"."
                move_num_str_next = str(move_num+1)+"."

                extr_len_indx = len(move_num_str)
                    
                p_1 = moves_left.find(move_num_str)
                p_2 = moves_left.find(move_num_str_next)

                #if last move to traverse (double_move means both white and black single move)
                if p_2 == -1:
                    double_move = moves_left[p_1+extr_len_indx:]
                    moves_traversed = True
                        

                #if not last move
                else:
                    double_move = moves_left[p_1+extr_len_indx:p_2]

                lim_1 = double_move.find(" ")
                white_moves_local_list.append(double_move[:lim_1])
                    
                black_move = double_move[lim_1+1:]
                lim_2 = black_move.find(" ")
                black_moves_local_list.append(black_move[:lim_2])

                moves_left = moves_left[p_2:]
                move_num += 1

            return white_moves_local_list, black_moves_local_list
            

        vars_list = []
        dictionary = {}

        work_data = text_data
        traversed_vars = False

        while traversed_vars == False:

            pos_open_br, pos_closed_br = work_data.find("("), work_data.find(")")

            #vars not traversed
            if pos_open_br != -1 and pos_closed_br != -1:
                new_variation = work_data[pos_open_br+1:pos_closed_br]
                vars_list.append(new_variation)

                work_data = work_data[pos_closed_br+1:]
                
                #this bit of code separates one side variation moves from untraversed ones
                next_br = work_data.find("(")
                if next_br != -1:
                    moves = work_data[:next_br]

                else:
                    moves = work_data

                white_moves, black_moves = produce_lists_of_moves_for_side_var(moves)
                
                dictionary[new_variation] = {"white": white_moves, "black": black_moves}

            #vars traversed
            else:
                traversed_vars = True

            
        return vars_list, dictionary

            