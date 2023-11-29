DROP PROCEDURE [dbo].[users_sp]
GO

CREATE PROC [dbo].[sp_users] (@pjsonfile VARCHAR(MAX), @action VARCHAR(2))
--INSERT --> 1
--UPDATE --> 2
--DELETE --> 3
AS

/*
DECLARE @pjsonfile VARCHAR(MAX) = '{
  "users": [
    {
      "user_id": 1,
      "email": "email@example.com",
	  "employee_number": "123",
	  "user_type_id": "1",
	  "user_type_action_id": "1"
    }
  ]
}',
@action VARCHAR(2) = '1'
*/

SET NOCOUNT ON

BEGIN
	DECLARE @Outputmessage VARCHAR(MAX) = '
	{
	  "result": [
		{
		  "value": "",
		  "msg": ""
		}
	  ]
	}',
	@Error VARCHAR(500) = ''

	--Insert
	IF @action = '1'
	BEGIN
		BEGIN TRY
			BEGIN TRAN
				INSERT INTO [dbo].[users] (email)
				SELECT
					JSON_VALUE(value, '$.email') AS email
				FROM OPENJSON(@pjsonfile, '$.users')
			COMMIT TRAN

			SET @Outputmessage = JSON_MODIFY(@Outputmessage, '$.result[0].value', '0');
			SET @Outputmessage = JSON_MODIFY(@Outputmessage, '$.result[0].msg', '');

		END TRY
		BEGIN CATCH
			ROLLBACK
			SET @ERROR = ERROR_MESSAGE()
			SET @Outputmessage = JSON_MODIFY(@Outputmessage, '$.result[0].result', '1')
			SET @Outputmessage = JSON_MODIFY(@Outputmessage, '$.result[0].msg', @Error)
		END CATCH
	END

	--Update

	IF @action = '2'
	BEGIN
		BEGIN TRY
			DECLARE @email varchar(50)
			DECLARE	@user_id INT

			SELECT
				@email = JSON_VALUE(value, '$.email'),
				@user_id = JSON_VALUE(value, '$.user_id')
			FROM
				OPENJSON(@pjsonfile, '$.users')

			BEGIN TRAN

				UPDATE [dbo].[users] SET
					email = @email
				WHERE
					[user_id] = @user_id

			COMMIT TRAN

			SET @Outputmessage = JSON_MODIFY(@Outputmessage, '$.result[0].value', '0');
			SET @Outputmessage = JSON_MODIFY(@Outputmessage, '$.result[0].msg', '');

		END TRY
		BEGIN CATCH
			SET @ERROR = @@ERROR
			SET @Outputmessage = JSON_MODIFY(@pjsonfile, '$.users[0].value', '1')
			SET @Outputmessage = JSON_MODIFY(@pjsonfile, '$.users[1].msg', @Error)
		END CATCH
	END
	/**/

	SELECT
		JSON_VALUE(value, '$.value') AS [value],
		JSON_VALUE(value, '$.msg') AS [msg]
	FROM OPENJSON(@Outputmessage, '$.result')

END
GO