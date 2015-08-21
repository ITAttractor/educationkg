Feature: Карта.
  При наведении на область отображается информация о количестве школ в этой области.

  Scenario Outline: Информация по количеству школ по областям
    Given пользователь открывает главную страницу
    When пользователь наводит курсор на область "<region>"
    Then видит количество школ "<total_schools>"
    Examples:
      | region           | total_schools |
      | state_chuy       | 320           |
      | state_issyk_kyl  | 206           |
      | state_naryn      | 141           |
      | state_jalal_abad | 456           |
      | state_osh        | 588           |
      | state_batken     | 225           |
      | state_talas      | 118           |
      | city_bishkek     | 135           |
