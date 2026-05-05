tempo 140

D4 q -> for i in 1..15
    E4 e -> if i % 15 == 0
        C5 s -> print "FizzBuzz"
    F4 e -> else if i % 3 == 0
        A4 s -> print "Fizz"
    G4 e -> else if i % 5 == 0
        B4 s -> print "Buzz"
    C4 q -> else
        C4 q -> print i

G4 w -> end
