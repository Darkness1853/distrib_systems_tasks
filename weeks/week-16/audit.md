# Security Audit Report

**project_code**: devices-s17

## Найденные проблемы

### 1. Отсутствие аутентификации
**Severity**: Critical

**Description**: Любой клиент может создавать и читать профили.

```python
@app.get("/api/profiles/")
def get_profiles():
    return profiles 
```
**Remediation**: нужно добавить JWT аутентификацию, проверять токен перед каждым запросом.

### 2. Отсутствие авторизации (IDOR)
**Severity**: High  

**Description**: Пользователь может получить все профили, включая чужие.

**Remediation**: нужно добавить проверку права доступа.

### 3. Отсутствие валидации входных данных
**Severity**: Medium

**Description**: Поля name, email, phone не валидируются перед сохранением.

```python
class ProfileCreate(BaseModel):
    name: str    
    email: str   
    phone: str    
```
**Remediation**: нужно добавить валидацию 

### 4. Отсутствие HTTPS
**Severity**: Medium

**Description**: Все запросы идут по HTTP, данные передаются в открытом виде.

**Remediation**: нужно настроить SSL сертификаты в Nginx, включить HTTPS.

### 5. Отсутствие rate limiting
**Severity**: Low

**Description**: Нет ограничения на количество запросов от одного клиента.

**Remediation**: Добавить лимиты

### 6. Хранение данных в памяти
**Severity**: Medium

**Description**: Профили хранятся в списке в памяти (profiles = [])

**Remediation**: Нужно использовать PostgreSQL или другую БД.
