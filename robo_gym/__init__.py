from gym.envs.registration import register

# naming convention: EnvnameRobotSim

# Example Environments
register(
    id='ExampleEnvSim-v0',
    entry_point='robo_gym.envs:ExampleEnvSim',
)

register(
    id='ExampleEnvRob-v0',
    entry_point='robo_gym.envs:ExampleEnvRob',
)

# UR Environments
register(
    id='EmptyEnvironmentURSim-v0',
    entry_point='robo_gym.envs:EmptyEnvironmentURSim',
)

register(
    id='EmptyEnvironmentURRob-v0',
    entry_point='robo_gym.envs:EmptyEnvironmentURRob',
)

register(
    id='EndEffectorPositioningURSim-v0',
    entry_point='robo_gym.envs:EndEffectorPositioningURSim',
)

register(
    id='EndEffectorPositioningURRob-v0',
    entry_point='robo_gym.envs:EndEffectorPositioningURRob',
)

register(
    id='BasicAvoidanceURSim-v0',
    entry_point='robo_gym.envs:BasicAvoidanceURSim',
)

register(
    id='BasicAvoidanceURRob-v0',
    entry_point='robo_gym.envs:BasicAvoidanceURRob',
)

register(
    id='AvoidanceRaad2022URSim-v0',
    entry_point='robo_gym.envs:AvoidanceRaad2022URSim',
)

register(
    id='AvoidanceRaad2022URRob-v0',
    entry_point='robo_gym.envs:AvoidanceRaad2022URRob',
)

register(
    id='AvoidanceRaad2022TestURSim-v0',
    entry_point='robo_gym.envs:AvoidanceRaad2022TestURSim',
)

register(
    id='AvoidanceRaad2022TestURRob-v0',
    entry_point='robo_gym.envs:AvoidanceRaad2022TestURRob',
)
