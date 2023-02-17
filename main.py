import os.path

import neat

from lib import *


def eval_genomes(genomes, config):
    _game = Game(720, 1280)
    for _id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        _game.add_player((net, genome))
    while not _game.isOver():
        _game.draw()


def run(_config_path):
    # load default config
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                neat.DefaultStagnation, _config_path)
    # create population
    population = neat.Population(config)
    # stdout
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    # start training
    # pass the fitness function for n generation
    winner = population.run(eval_genomes, n=50)

    print(f"the winner is {winner}")


if __name__ == "__main__":
    # load config file of neat
    cwd = os.path.dirname(__file__)
    config_path = os.path.join(cwd, "config-feedforward")
    run(config_path)
