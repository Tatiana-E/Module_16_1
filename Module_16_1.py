from fastapi import FastAPI


# Создаем экземпляр приложения FastAPI
app = FastAPI()
# Определение базового маршрута

@app.get("/user/admin")
async def admin_root():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_root(user_id: int)->str:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def user_root(username: str, age: int) ->str:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

@app.get("/")
async def root():
    return {"message": "Главная страница"}

