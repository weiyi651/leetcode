# V1
# 执行用时：48 ms, 在所有 Python3 提交中击败了24.05%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了16.52%的用户
def is_front_bracket(character, bracket_set):
    if character in {i[0] for i in bracket_set}:
        return True
    else:
        return False

def is_back_bracket(character, bracket_set):
    if character in {i[-1] for i in bracket_set}:
        return True
    else:
        return False

def update_parenthese_dict(character, parentheses_dict, bracket_type):
    if bracket_type=='front':
        parentheses_dict['front'].append(character)
    elif bracket_type =='back':
        parentheses_dict['back'].append(character)
        parentheses_dict['front'].pop()


def is_valid(character, parentheses_dict):
    if parentheses_dict['front']:
        last_front_bracket = parentheses_dict['front'][-1]
        combined_parenthese = last_front_bracket + character
        if combined_parenthese in parentheses_dict['type']:
            return True
        else:
            return False
    else:
        return False


class Solution:   
    def isValid(self, s: str) -> bool:
        parentheses_dict = {'type':['()',"{}","[]"],'front':[],'back':[]}
        for character in s:
            if is_front_bracket(character, parentheses_dict['type']):
                update_parenthese_dict(character, parentheses_dict, 'front')
            elif is_back_bracket(character, parentheses_dict['type']):
                if is_valid(character,parentheses_dict):
                    update_parenthese_dict(character, parentheses_dict, 'back')
                else:
                    return False
            else:
                pass
        if parentheses_dict['back'] and not parentheses_dict['front']:
            return True
        else:
            return False

