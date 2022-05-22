"""
������� 4.
��� ���� ������:
1) ���������� 2-3 ������� (����������� � ��������� ����������)
2) ������� ��������� ������� ��������� � ���� �������� � ������� �-�������
3) ������� �������� ��������� ������� ������� � ������� �-�������
4) �������� �����, ����� ������� ����������� � ������
���� ������:
������������ ���-������� �������� ��������������.
� ������� �������� �����, ������ � ������� �� ��������� ������� ������.
����� ����������� ��������, ����� �� ������������ ���� ������� � �������.
��� ���� ��� ������ ������ ���� ������������.
� ���� ���, �� �����-�� ����� ���������� �� ������.
���������� ������ ������ ������ �� ��� �������
 � ���� ����������� � ���� �������.
��� ���������� ��������� ����� ��������� ����� ������,
������� �� ����������, ��������, ��������� �������.
����������: ����� ��� ����������� ������ �������!
"""

dict_user = {'login1': ['1234', False], 'login2': ['134', False], 'login3': ['234', True], 'login4': ['1234', False]}

def check_user_1(dict_user, login_in, pass_in): # O(n)
# ��������������� ��������� ��� ������� ������������    
    for login in dict_user.keys(): # O(n)
        if login == login_in: # O(1)
            if dict_user[login][1]: # O(1)
                if dict_user[login][0] == pass_in: # O(1)
                    return '�������' # O(1)
                else:
                    return '������ � ������ ��� ������' # O(1)
            else:
                return '����������� �������' # O(1)
    return '����������� �����' # O(1)

print(check_user_1(dict_user, '', ''))
print(check_user_1(dict_user, 'login1', ''))
print(check_user_1(dict_user, 'login3', ''))
print(check_user_1(dict_user, 'login3', '234'))

##########################

def check_user_2(dict_user, login_in, pass_in): # O(n**2)
    for login in dict_user.keys(): # O(n)
        if login == login_in: # O(1)
            for item in dict_user.items():
                if item[0] == login:
                    if item[1][1]:
                        if item[1][0] == pass_in:
                            return '�������' # O(1)
                        else:
                            return '������ � ������ ��� ������' # O(1)
                    return '����������� �������' # O(1)
    else:        
        return '����������� �����' # O(1)
    return login

print(check_user_2(dict_user, '', ''))
print(check_user_2(dict_user, 'login1', ''))
print(check_user_2(dict_user, 'login3', ''))
print(check_user_2(dict_user, 'login3', '234'))

# ������� check_user_1 ����� ������� ��������� (O(n) < O(n**2)), ������� �����������
