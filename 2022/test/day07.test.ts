import {FileElement, Cli, FileInput} from '../src/day07'

describe('FileElement should', () => {
    it('have test run', () => {
        let elmnt = new FileElement('/', 0)

        expect(elmnt).not.toBeNull()
    })

})

describe('Cli should', () => {
    it('have test run', () => {
        let cli = new Cli()

        expect(cli).not.toBeNull()
    })
    it('change to root', () => {
        let cli = new Cli()
        cli.ChangeDir('/')

        expect(cli.GetCurrentDir()).toBe('/')
    })
    it('list all files', () => {
        let cli = new Cli()
        let l = cli.List()

        expect(l).toStrictEqual([])
        expect(cli.GetCurrentDir()).toBe('/')
    })
    it('add dir', () => {
        let cli = new Cli()
        cli.AddDir('a')
        let l = cli.List()

        expect(l).toStrictEqual(['a'])
    })
    it('add file', () => {
        let cli = new Cli()
        cli.AddFile('b.txt', 14848514)
        let l = cli.List()

        expect(l).toStrictEqual(['b.txt'])
    })
    it('change to subdir', () => {
        let cli = new Cli()
        cli.AddDir('a')
        cli.ChangeDir('a')
        let l = cli.List()

        expect(l).toStrictEqual([])
    })

    it('change nonexistent subdir', () => {
        let cli = new Cli()
        cli.ChangeDir('a')
  
        let l = cli.List()

        expect(l).toStrictEqual([])
        expect(cli.GetCurrentDir()).toBe('a')
    })

    it('get size of dir', () => {
        let cli = new Cli()
        cli.AddDir('a')
        cli.ChangeDir('a')
        cli.AddFile('b.txt', 14848514)
        expect(cli.GetCurrentDirSize()).toBe(14848514)
    })
    it('change to parent dir', () => {
        let cli = new Cli()
        cli.AddDir('a')
        cli.ChangeDir('a')
        cli.ChangeDir('..')
        let l = cli.List()

        expect(l).toStrictEqual(['a'])
        expect(cli.GetCurrentDir()).toBe('/')
    })
    it('get size of root', () => {
        let cli = new Cli()
        cli.AddDir('a')
        cli.AddFile('b.txt', 200)
        cli.ChangeDir('a')
        cli.AddFile('b.txt', 300)
        cli.ChangeDir('/')
        expect(cli.GetCurrentDirSize()).toBe(500)
    })

    it('parse command line to change dir', () => {
        let cli = new Cli()
        cli.ParseLine('$ cd /')

        expect(cli.GetCurrentDir()).toBe('/')
    })

    it('parse command line to list dir', () => {
        let cli = new Cli()
        cli.ChangeDir('c')
        cli.ParseLine('$ ls')
        cli.ParseLine('dir a')
        cli.ParseLine('200 b.txt')

        expect(cli.List()).toStrictEqual(['a','b.txt'])
        expect(cli.GetCurrentDirSize()).toBe(200)
    })

    it('return correct size for test data', () => {
        let cli = new Cli()
        let input = new FileInput('../test/input/day07.txt')
        input.data.forEach(line => {
            cli.ParseLine(line)
        })
        cli.ChangeDir('/')

        expect(cli.GetCurrentDirSize()).toBe(48381165)
    })
})