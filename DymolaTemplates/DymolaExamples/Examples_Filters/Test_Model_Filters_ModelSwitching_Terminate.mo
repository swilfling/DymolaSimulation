within DymolaExamples.Examples_Filters;
model Test_Model_Filters_ModelSwitching_Terminate
  parameter Real fmi_NumberOfSteps = 1000;
  parameter Real fmi_StartTime=0;
  parameter Real fmi_StopTime=10;
  parameter Real y_start=0;
  Modelica.Blocks.Sources.Step InputSignal(
    startTime=0.1,
    height=1,
    offset=0)
             annotation (Placement(transformation(extent={{-84,0},{-64,20}})));
  Modelica.Blocks.Math.Feedback error_calc annotation (Placement(transformation(extent={{10,4},{
            30,24}})));
  TestbenchComponents.Threshold_Terminator threshold_Terminator(threshold=
       0.1)
           annotation (Placement(transformation(extent={{50,0},{70,20}})));
      Chebyshev_fmu UUT(y_start=y_start, fmi_NumberOfSteps=fmi_NumberOfSteps,
    fmi_StartTime=fmi_StartTime, fmi_StopTime=fmi_StopTime)
                                                           annotation (Placement(transformation(extent={{-30,0},
            {-10,20}})));
equation

  connect(InputSignal.y, UUT.u1)
                                annotation (Line(points={{-63,10},{-41.28,10},{
          -41.28,10},{-30.4,10}},                             color={255,127,
          0}));
  connect(UUT.y1, error_calc.u1)
                                annotation (Line(points={{-8,15},{2,15},{2,14},
          {12,14}},                                           color={255,127,
          0}));
  connect(error_calc.u2, UUT.u1)
                                annotation (Line(points={{20,6},{20,-16},{-46,
          -16},{-46,10},{-30.4,10}},                          color={255,127,
          0}));
  connect(error_calc.y, threshold_Terminator.u1)
                                                annotation (Line(points={{29,14},
          {40,14},{40,8.4},{48,8.4}},                         color={255,127,
          0}));
end Test_Model_Filters_ModelSwitching_Terminate;
