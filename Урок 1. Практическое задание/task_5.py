"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""
public class Stack
{
    LinkedList _items = new LinkedList();
    public void Push(T value)
    {
        throw new NotImplementedException();
    }
    public T Pop()
    {
        throw new NotImplementedException();
    }
    public T Peek()
    {
        throw new NotImplementedException();
    }
    public int Count
    {
        get;
    }
}


public void Push(T value)
{
    _items.AddLast(value);
}
public T Pop()
{
    if (_items.Count == 0)
    {
        throw new InvalidOperationException("The stack is empty");
    }
    T result = _items.Tail.Value;
    _items.RemoveLast();
    return result;
}
# Сложность: O(1)

public int Count
{
    get
    {
        return _items.Count;
    }
}
# Сложность: O(1)
