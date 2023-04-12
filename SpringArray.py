from Spring import Spring


class SpringArray:

    @staticmethod
    def equivalentSpring(springExpr):
        """
        Static method that takes a string expression that represents connections of springs of unit stiffness
        and returns the equivalent spring.

        springExpr: String expression of balanced braces {} and brackets [] representing the connections of springs
                    of unit stiffness.

        Returns: A Spring object representing the equivalent spring.
        """
        # Stack to keep track of the springs
        stack = []

        # Loop through the characters in the string expression
        for char in springExpr:
            # If the character is an opening brace or bracket, push a new Spring object to the stack
            if char in {'{', '['}:
                stack.append(Spring())

            # If the character is a closing brace or bracket, connect the top two springs in the stack
            elif char in {'}', ']'}:
                # If the stack has less than 2 springs, the expression is invalid
                if len(stack) < 2:
                    raise ValueError('Invalid expression')

                # Pop the top two springs from the stack
                spring2 = stack.pop()
                spring1 = stack.pop()

                # If the closing character is a brace, connect the two springs in series
                if char == '}':
                    new_spring = spring1.in_series(spring2)
                # If the closing character is a bracket, connect the two springs in parallel
                else:
                    new_spring = spring1.in_parallel(spring2)

                # Push the new spring to the stack
                stack.append(new_spring)

        # If the stack has more than 1 spring, the expression is invalid
        if len(stack) > 1:
            raise ValueError('Invalid expression')

        # Return the remaining spring as the equivalent spring
        return stack[0] if stack else Spring()

    @staticmethod
    def equivalentSpring(springExpr, springs):
        """
        Static method that takes a string expression that represents connections of springs specified by a Spring
        array and returns the equivalent spring.

        springExpr: String expression of balanced braces {} and brackets [] representing the connections of springs.
        springs: An array of Spring objects representing the individual springs that can be used in the expression.

        Returns: A Spring object representing the equivalent spring.
        """
        # Map the spring objects to their corresponding characters
        spring_map = {}
        for i, spring in enumerate(springs):
            spring_map[str(i)] = spring

        # Stack to keep track of the springs
        stack = []

        # Loop through the characters in the string expression
        for char in springExpr:
            # If the character is a number, push the corresponding spring to the stack
            if char.isdigit():
                spring = spring_map[char]
                stack.append(spring)

            # If the character is an opening brace or bracket, push a new Spring object to the stack
            elif char in {'{', '['}:
                stack.append(Spring())

            # If the character is a closing brace or bracket, connect the top two springs in the stack
            elif char in {'}', ']'}:
                # If the stack has less than 2 springs, the expression is invalid
                if len(stack) < 2:
                    raise ValueError('Invalid expression')

                # Pop the top two springs from the stack
                spring2 = stack.pop()
                spring1 = stack.pop()

                # If the closing character is a brace, connect the two springs in series
                if char == '}':
                    new_spring = spring1.in_series(spring2)
                # If the closing character is a bracket, connect the two springs in parallel
                else:
                    new_spring = spring1.in_parallel(spring2)

                # Push the new spring to the stack
                stack.append(new_spring)

        # If the stack has more than 1 spring, the expression is invalid
        if len(stack) > 1:
            raise ValueError('Invalid expression')

        # Return the remaining spring as the equivalent spring
        return stack[0] if stack else Spring()