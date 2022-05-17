within DymolaExamples.Examples_Filters;
model Test_Model_Filters

  replaceable Modelica.Blocks.Sources.Sine InputSignal(
    amplitude=1,
    freqHz=1,                                          startTime=0.1, offset=
        0.1) constrainedby Modelica.Blocks.Interfaces.SignalSource(startTime=
        0.1, offset=0.1)
            annotation (Placement(transformation(extent={{-76,28},{-56,48}})));
  Modelica.Blocks.Interaction.Show.RealValue realValue2
    annotation (Placement(transformation(extent={{52,2},{72,22}})));
  Model_Filters model_Filters
    annotation (Placement(transformation(extent={{-22,-6},{10,26}})));
  Modelica.Blocks.Sources.IntegerConstant filterSelect(k=1)
    annotation (Placement(transformation(extent={{-78,-12},{-58,8}})));
equation
  connect(model_Filters.select,filterSelect. y) annotation (Line(points={{-20.56,
          -2.32},{-41.28,-2.32},{-41.28,-2},{-57,-2}},        color={255,127,
          0}));
  connect(InputSignal.y,model_Filters. u) annotation (Line(points={{-55,38},{
          -34,38},{-34,19.12},{-20.24,19.12}}, color={0,0,127}));
  connect(model_Filters.y,realValue2. numberPort) annotation (Line(points={{8.72,
          12.88},{50.5,12.88},{50.5,12}},      color={0,0,127}));
end Test_Model_Filters;
