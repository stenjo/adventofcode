using SafeTestsets

@safetestset "Main.Day01" begin
    using Main.Day01

    @testset "part1" begin
        using Main.Day01: part1
        @test part1([1721,979,366,299,675,1456]).mem.vect == 514579
    end
end
