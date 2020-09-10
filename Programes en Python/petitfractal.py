import turtle

def tree(branch, t):
    if branch > 0:
        t.forward(branch*15)
        t.right(20)
        tree(branch-1,t)
        t.left(40)
        tree(branch-1,t)
        t.right(20)
        t.backward(branch*15)

def main():
    t = turtle.Turtle()
    numBranches = 6

    t.left(90)
    t.up()
    t.backward(250)
    t.down()
    t.color("purple")
    tree(6, t)

    turtle.done()

main()
