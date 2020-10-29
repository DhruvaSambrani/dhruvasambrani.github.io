name = "Dhruva Sambrani"
l = [""]

for i in name
    k = l[end]
    push!(l, map(x -> k * x, rand('A':'z', 4))...)
    push!(l, k * i)
end
println("keyframes: [")
for i in l
    println("  {innerHTML: \"\$ $(i)|\"},")
end
println("]")
