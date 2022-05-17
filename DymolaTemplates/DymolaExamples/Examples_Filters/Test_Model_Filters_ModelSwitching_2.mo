within DymolaExamples.Examples_Filters;
model Test_Model_Filters_ModelSwitching_2
  parameter Real fmi_NumberOfSteps = 100;
  parameter Real fmi_StartTime=0;
  parameter Real fmi_StopTime=10;
  Modelica.Blocks.Interaction.Show.RealValue Output_Model_Filters;
 Modelica.Blocks.Sources.Pulse InputSignal(
                                    startTime=0.1, period=2,  offset=0.1)
    annotation (Placement(transformation(extent={{-88,48},{-68,68}})));
  Modelica.Blocks.Routing.Multiplex2 multiplex2_1
    annotation (Placement(transformation(extent={{20,44},{40,64}})));
  Modelica.Blocks.Routing.Extractor filter_output(
    nin=2,
    allowOutOfRange=true,
    outOfRangeValue=1)
    annotation (Placement(transformation(extent={{62,44},{82,64}})));
  Modelica.Blocks.Sources.IntegerConstant selector(k=1)
    annotation (Placement(transformation(extent={{-64,-56},{-44,-36}})));
    Chebyshev_fmu UUT(fmi_StartTime=fmi_StartTime, fmi_StopTime=fmi_StopTime);
    Butterworth_fmu UUT2(fmi_StartTime=fmi_StartTime, fmi_StopTime=fmi_StopTime);
equation
   connect(UUT2.u1, InputSignal.y) annotation (Line(points={{-26.4,12},{-48,12},
          {-48,58},{-67,58}},color={0,0,127}));
  connect(UUT.u1, InputSignal.y)
    annotation (Line(points={{-28.4,56},{-48,56},{-48,58},{-67,58}},
                                                   color={0,0,127}));
  connect(UUT.y1, multiplex2_1.u1[1])
    annotation (Line(points={{-6,61},{8,61},{8,60},{18,60}}, color={0,0,127}));
  connect(multiplex2_1.y, filter_output.u)
    annotation (Line(points={{41,54},{60,54}}, color={0,0,127}));
  connect(selector.y, filter_output.index)
    annotation (Line(points={{-43,-46},{72,-46},{72,42}}, color={255,127,0}));
  connect(UUT2.u1, InputSignal.y) annotation (Line(points={{-26.4,12},{-48,12},
          {-48,58},{-67,58}}, color={0,0,127}));
  connect(UUT2.y1, multiplex2_1.u2[1])
    annotation (Line(points={{-4,17},{8,17},{8,48},{18,48}}, color={0,0,127}));
end Test_Model_Filters_ModelSwitching_2;
