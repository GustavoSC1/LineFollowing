from controller import Robot

def run_robot(robot):
    
    time_step = 32
    max_speed = 6.28
    
    # motores
    left_motor = robot.getDevice('re')
    right_motor = robot.getDevice('rd')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)    
    
    # ativar sensores infravermelho
    left_ir = robot.getDevice('ds_seguidor_de_linha3')
    left_ir.enable(time_step)
    
    right_ir = robot.getDevice('ds_seguidor_de_linha1')
    right_ir.enable(time_step)
    
    middle_ir = robot.getDevice('ds_seguidor_de_linha2')
    middle_ir.enable(time_step)
    
    # ativar sensor ultrassom
    front_sonar = robot.getDevice('ds_ultrassom2')
    front_sonar.enable(time_step)
                
    while robot.step(time_step)  != -1:
        
        # ler sensores infravermelhos
        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()
        middle_ir_value = middle_ir.getValue()
        
        # ler sensor ultrassom
        front_wall_value = front_sonar.getValue()         
        
        # if/else aqui
        
def delay_function(robot, tempo):
    current_time_1 = float(robot.getTime())
    current_time_2 = float(robot.getTime())
    
    # while aqui

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)