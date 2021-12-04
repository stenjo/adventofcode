

function Paper(file="day02.txt")
    lines=readlines(file)
    paper = 0
    for present in lines
        l,w,h = parse.(Int,split(present, 'x'))
        paper += 2*l*w+2*w*h+2*h*l+minimum([l*w, w*h, h*l])
    end
    println(paper)
end

function Ribbon(file="day02.txt")
    lines=readlines(file)
    ribbon = 0
    for present in lines
        l,w,h = parse.(Int,split(present, 'x'))
        ribbon += minimum([2*(l+w), 2*(w+h), 2*(h+l)])+(l*w*h)
    end
    println(ribbon)
end


Paper()
Ribbon()
