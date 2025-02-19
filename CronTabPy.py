from crontab import CronTab

# Crear objeto crontab para el usuario actual
cron = CronTab(user=True)

# Crear una nueva tarea
job = cron.new(command='python3 /home/dam50/miscript.py')

# Configurar para que se ejecute cada minuto
job.minute.every(1)

# Guardar cambios
cron.write()

print("Tarea creada correctamente")