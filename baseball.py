class Solution:
    def calPoints(self, operations: list) -> int:
        record = []

        for i in operations:
            if i == "+":
                record.append(record[-1] + record[-2])
            elif i == "D":
                record.append(record[-1]*2)
            elif i == "C":
                record.pop()
            else:
                record.append(int(i))
        
        sum = 0
        for i in record:
            sum += i
        
        return sum

    def evalRPN(self, tokens: list) -> int:
        num_stack = []

        op1 = None
        op2 = None
        for i in tokens:
            if i == "+":
                num_stack.append(num_stack.pop() + num_stack.pop())
            elif i == "-":
                num_stack.append(-1*num_stack.pop() + num_stack.pop())
            elif i == "*":
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif i == "/":
                op2 = num_stack.pop()
                op1 = num_stack.pop()
                num_stack.append(int(op1 / op2))

            else:
                num_stack.append(int(i))
        
        return num_stack.pop()

    res_list = [0,1]

    def fib(self, n: int) -> int:
        if n < len(self.res_list):
            return self.res_list[n]
        
        if n >= len(self.res_list):
            self.res_list.append(self.fib(n-1) + self.fib(n-2))
            return self.res_list[-1]
        

def main():
    bob = Solution()
    print(bob.fib(2))
    print(bob.fib(3))
    print(bob.fib(4))
    print(bob.fib(5))

if __name__ == "__main__":
    main()